def registrar_usuario(data):
    usuario = {}
    user = data
    doc = input("Ingresa el ID: ")
    if doc not in user:
        usuario["nombre"] = input("Ingresa el nombre: ")
        usuario["email"] = input("Ingresa el email: ")
        usuario["tel"] = input("Ingresa el telefono: ")
        usuario["ciudad"] = input("Ingresa la ciudad: ")
        usuario["edad"] = int(input("Ingresa la edad: "))
        usuario["carrito"] = []
        user[doc] = usuario
        print("Usuario registrado con exito!")
        print(user)
    else:
        print("El usuario ya existe!")

def leer_usuarios(data):
    for doc, info in data:
        nombre = info["nombre"]
        email = info["email"]
        tel = info["tel"]
        ciudad = info["ciudad"]
        edad = info["edad"]
        print(f"ID: {doc}, nombre: {nombre}, email: {email}, telefono: {tel}, ciudad: {ciudad}, edad: {edad}")

hm = {
    "1005327319" : {
        "nombre" : "adrian",
        "email" : "adrian@gmail.com",
        "tel" : "3173109599",
        "ciudad" : "bucaramanga",
        "edad" : 20,
        "carrito" : [
            {
                "nombre_producto" : "jean",
                "talla" : "36",
                "cantidad" : 1,
                "color" : "azul"
            }
        ]
    }
}

menu = ("1. Registrar usuario", "2. Leer usuarios", 
        "3. Agregar productos al carrito", "4. Leer productos del carrito", 
        "5. Eliminar usuario", "6. Eliminar productos del carrito", "7. Editar producto", "0. Salir")

submenu = ("1. Cambiar talla", "2. Aumentar cantidad", "3. Cambiar color")

while True:
    for i in menu:
        print(i)
    opt = int(input("Que deseas hacer? "))
    if opt == 0:
        print("Adios...")
        break
    elif opt == 1:
        registrar_usuario(hm)
    elif opt == 2:
        leer_usuarios(hm)
    