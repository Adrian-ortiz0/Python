# Write your solution here
word = input("Please type in a string: ")
i = 0
while i < len(word) - 1:
    
    if word[1] == word[i]:
        same = True
    else:
        same = False
    i += 1

if same:
    print(f"The second and the second to last characters are {word[1]}")
else:
    print("The second and the second to last characters are different")