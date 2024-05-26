productos = {
    "Menta": 300,
    "Chocorramo": 1000,
    "Esfero": 2700,
    "Chocolatina":2500
}

opciones_menu = ("1. Para comprar", "2. Para salir")

while True:
    for i in opciones_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    if opc == 2:
        print("Saliendo...")
        break
    else:
        print("*****************************************************")
        cont = 1
        print("Ingrese")
        for clave, valor in productos.items():
            print(cont, "para comprar", clave, "que tiene un precio de", valor)
            cont += 1
        opc_producto = int(input("Ingrese la opción deseada: "))
        cont = 1
        llave = ""
        for i in productos:
            if opc_producto == cont:
                llave = i
            cont += 1
        if llave != "":
            valor = productos[llave]
            cantidad = int(input("Ingrese la cantidad de productos: "))
            total = valor * cantidad
            print("El total es", total)
        else:
            print("Producto no existe")
        print("*****************************************************")