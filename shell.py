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



# shell.py
from flask import Flask, request, jsonify
import basica

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_code():
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
    app.run(host="0.0.0.0", port=5000)


