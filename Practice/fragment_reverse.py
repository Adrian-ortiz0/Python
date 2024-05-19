# Write your solution here
deci = input("Do you want to invert the word? (y/n)")
if deci == "n":
    
    word = input("Please type in a string: ")
    i = 0
    leng = len(word)

    while i <= leng:
        print(word[0:i])
        i += 1
elif deci == "y":
    

    word_2 = input("Please type in a string: ")
    j = len(word_2)
    while j >= 0:
        print(word_2[j:])
        j -= 1

else:
    print("invalid command!")