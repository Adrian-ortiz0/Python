word = input("Type in a word: ")
subw = input("Please type in a character: ")
fing = word.find(subw)
i = 0

while i < len(word)-2:
    if word[i] == subw:
        print(word[i:i+3])
        break
    i += 1