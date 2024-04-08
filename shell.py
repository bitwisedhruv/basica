import basica

while True:
    text = input("> ")
    if text.strip() == "":
        continue
    result, error = basica.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(result.elements[0])
        else:
            print(repr(result))
