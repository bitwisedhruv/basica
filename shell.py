import basica

while True:
    text = input("> ")
    result, error = basica.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        print(repr(result))
