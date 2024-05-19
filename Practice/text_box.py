word = input("Word: ")
stars = "*" * 30
i = 0
leng = len(word)
while i < 2:
    print(stars)
    i += 1
    if i == 1:
        spaces_b = (28 - leng) // 2
        spaces_e = spaces_b
        if len(word) % 2 != 0:
            spaces_e += 1
        print(("*" + " " * spaces_b + word + " " * spaces_e + "*"))
