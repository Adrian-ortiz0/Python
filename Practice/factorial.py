#Factorial exercise

num = int(input("Type in a num: "))
i = 1
result = 1

while i <= num:
    if num > 0:
        result *= i
    i += 1
print(result)