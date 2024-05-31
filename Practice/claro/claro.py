import json

def cargar_datos():
    
    try:
        with open("claro/usuarios.json", "r") as file:
            data = json.load(file)
            print("Datos cargados exitosamente!")
            return data
    except Exception:
        print("Error al cargar datos")
                

def guardar_datos(data):
    try:
        json_string = json.dumps(data, indent=4)
        with open("claro/usuarios.json", "w") as file:
            file.write(json_string)
        print("Datos guardados exitosamente en 'claro/usuarios.json'.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def registrar_usuarios(data):
    
    print("*****************************************************************************")
    
    usuario = {}
    documento ={}
    doc = input("Ingrese su documento: ")
    for i in range(len(data["usuarios"])):
        if doc in (data["usuarios"][i]):
            print("ya esiste")
        else:
            usuario["nombre"] = input("ingrese su nombre: ")
            usuario["edad"] = int(input("ingrese su edad: "))
            usuario["correo"] = input("ingrese su correo: ")
            documento[doc] = usuario
            data["usuarios"].append(documento)
            print("usuario creado con exito!")
            guardar_datos(data)
            print("******************************************************************************")
            
            print(data["usuarios"])
            respuesta = input("¿Desea registrar otro usuario? (s/n): ")
            if respuesta.lower() != 's':
                    break  # Salir del bucle si la respuesta no es 's'
    print("******************************************************************************")
            

def editar_usuarios(data):
    print(data["usuarios"][0]["1005327319"])
    doc = input("Ingrese su documento: ")
    for i in range(len(data["usuarios"])):
        if doc in (data["usuarios"][i]):
            data["usuarios"][i][doc]["nombre"] = input("nuevo nombre: ")
            data["usuarios"][i][doc]["edad"] = int(input("nueva edad: "))
            data["usuarios"][i][doc]["correo"] = input("nuevo correo: ")
            guardar_datos(data)
            
        else:
            print("no esiste")

def mostrar_usuarios(data):
    #print(data["usuarios"][0]["1005327319"])
    for i in range(len(data["usuarios"])):
        print(data["usuarios"][i].values())
        

claro = {
    "usuarios" : [
        {
            "1005327319" : {
                "nombre" : "Jhordan",
                "edad" : 17,
                "correo" : "jhordan@gmail.com"
            },
            "1097495965" : {
                "nombre" : "Adrian",
                "edad" : 17,
                "correo" : "adrian@gmail.com"
            }
        }
    ]
}






claro = cargar_datos()
menu = ("1. Registrar usuarios", "2. Editar usuario", "3. Mostrar usuarios", "4. Eliminar usuario", "0. Salir")
while True:
    for i in menu:
        print(i)
    opt = int(input("Elija una opcion: "))
    if opt == 0:
        break
    elif opt == 1:
        registrar_usuarios(claro)
    elif opt == 2:
        editar_usuarios(claro)
    elif opt == 3:
        mostrar_usuarios(claro)
    elif opt == 4:
        print("soy la opcion 2")           

