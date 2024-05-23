word = input("Type in a word: ")

if word == word[::-1]:
    print("palindromo")
else:
    print("not palindromo")