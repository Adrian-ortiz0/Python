count100k = 0
count50k = 0
count20k = 0
count10k = 0

while True:
    opt = input("Do you want to do a withdraw? (y/n)")
    if opt == "n":
        break
    else:   
        amount = int(input("Type amount: "))

        if amount < 10000 or amount % 10000 != 0:
            print("Invalid value")
        else:
            count100k = amount // 100000
            resto = amount % 100000
            count50k = resto // 50000
            resto = resto % 50000
            count20k = resto // 20000
            resto = resto % 20000
            count10k = resto // 10000
    print(f"{count100k} de 100")
    print(f"{count50k} de 50")
    print(f"{count20k} de 20")
    print(f"{count10k} de 10")
