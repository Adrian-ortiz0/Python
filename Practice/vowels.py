word = input("Type word: ")

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for i in word.lower():
    if i == "a":
        count_a += 1
    elif i == "e":
        count_e += 1
    elif i == "i":
        count_i += 1
    elif i == "o":
        count_o += 1
    elif i == "u":
        count_u += 1

print(f"la palabra {word} tiene {count_a} a")
print(f"la palabra {word} tiene {count_e} e")
print(f"la palabra {word} tiene {count_i} i")
print(f"la palabra {word} tiene {count_o} o")
print(f"la palabra {word} tiene {count_u} u")

    
