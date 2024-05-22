def mcd (num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

num1 = int(input("Type num 1: "))
num2 = int(input("Type num 2: "))

def mcm(num1, num2):
    return (num1 * num2) // mcd(num1, num2)

print("El MCM de", num1, "y", num2, "es:", mcm(num1, num2))
print(f"El MCD de {num1} y {num2} es: {mcd(num1,num2)}")