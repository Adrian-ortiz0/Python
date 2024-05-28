participantes_patinaje = {  
    "1005327319" : {
            "nombre" : "adrian", "edad" : 18, "departamento" : "santander"
    },
    
    "741852963" : {
            "nombre" : "daniel", "edad" : 21, "departamento" : "antioquia"        
    }
}

def registrar_usuarios(data):     
    
    participante = {}
    doc = input("Ingresa el documento: ")
    if data.get(doc, None) == None:
        participante["nombre"] = input("Ingresa el nombre: ")
        participante["edad"] = int(input("Ingresa la edad: "))
        participante["departamento"] = input("Ingresa tu departamento: ")
        
        if participante["edad"] < 18 or participante["departamento"] != "santander" :
            print("Debes ser mayor de 18 o de Santander para poder participar")
        else:
            data[doc] = participante
            print("Registro exitoso!")
    else:
            print("participante ya existe!")

def mostrar_usuarios(data):
    for i in data:
        print(data[i])

def ranking(data):
    for i in range(0, 4):
        print(data[i])