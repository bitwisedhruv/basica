# import basica

# while True:
#     text = input("> ")
#     if text.strip() == "":
#         continue
#     result, error = basica.run("<stdin>", text)

#     if error:
#         print(error.as_string())
#     elif result:
#         if len(result.elements) == 1:
#             print(repr(result.elements[0]))
#         else:
#             print(repr(result))

from flask import Flask, request, jsonify
from flask_cors import CORS
import basica
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Basica API. Use POST /run with {'code': 'your code'} to execute Basica code."
    }), 200

@app.route("/run", methods=["POST"])
def run_code():
    if not request.is_json:
        return jsonify({"result": "", "error": "Request must be JSON"}), 400
    text = request.json.get("code", "")
    if not text.strip():
        return jsonify({"result": "", "error": "Empty input"}), 400
    
    result, error = basica.run("<stdin>", text)
    
    if error:
        return jsonify({"result": "", "error": error.as_string()}), 200
    elif result:
        if len(result.elements) == 1:
            return jsonify({"result": repr(result.elements[0]), "error": ""}), 200
        else:
            return jsonify({"result": repr(result), "error": ""}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)