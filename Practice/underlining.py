while True:
    word = input("Please type in a string: ")
    leng = len(word)
    if word == "":
        break

    print(word)
    print("-" * leng)