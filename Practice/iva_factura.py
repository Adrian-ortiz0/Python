def factura_iva(amount,iva):
    if iva != 0 and iva > 0:
        iv = amount * (iva/100)
        result = amount + iv
        print(result)
    else:
        iv = amount * (21/100)
        result = amount + iv
        print(result)



amount = int(input("Type amount: "))
iva = int(input("Type iva: "))
factura_iva(amount,iva)