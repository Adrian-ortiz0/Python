def registrar_estudiante(data):
    estudiante = {}
    materias = {}
    trimestres = {}
    stu = data["estudiantes"]
    doc = input("Ingresa el documento: ")
    if stu.get(doc, None) == None:
        estudiante["nombre"] = input("Escribe el nuevo nombre: ")
        while True:
            materia = input("Nombre de la materia: ")
            
            trimestres["trimestre 1"] = int(input("Ingrese nota del trimestre 1: "))
            trimestres["trimestre 2"] = int(input("Ingrese nota del trimestre 2: "))
            trimestres["trimestre 3"] = int(input("Ingrese nota del trimestre 3: "))
            
            materias[materia] = trimestres
            estudiante["materias"] = materias
            stu[doc] = estudiante
            
            opt = input("Desea agregar otra materia? (si/no): ")
            if opt == "no":
                print("Okay")
                break
            elif opt == "si":
                continue               
        print(stu)
    else:
        print("Ese usuario ya existe!")

def añadir_materia(data):
    trimestres = {}
    stu = data["estudiantes"]
    doc = input("Ingresa tu documento: ")
    if stu.get(doc, None) != None:
        existing = stu[doc]["materias"]
        stu[doc]["materias"] = existing
        while True:
            opt = input("Desea agregar otra materia? (si/no): ")
            if opt == "no":
                print("Okay!")
                break
            elif opt == "si":
                 materia = input("Nombre de la materia: ")
            
            trimestres["trimestre 1"] = int(input("Ingrese nota del trimestre 1: "))
            trimestres["trimestre 2"] = int(input("Ingrese nota del trimestre 2: "))
            trimestres["trimestre 3"] = int(input("Ingrese nota del trimestre 3: "))
            
            stu[doc][materia] = trimestres
    else:
        print("el estudiante no existe!")    
        
    print(stu[doc])
    
def actualizar_nota(data):
    stu = data["estudiantes"]
    doc = input("Ingrese el documento: ")
    if stu.get(doc, None) != None:
        print(stu[doc]["materias"])
        mt = input("Nombre de materia que deseas modificar: ")
        print(stu[doc]["materias"][mt])
        trimestre = input("Trimestre que desees cambiar su nota: ")
        print(stu[doc]["materias"][mt][trimestre])
        stu[doc]["materias"][mt][trimestre] = int(input("Nueva nota: "))
        print(stu[doc]["materias"][mt])
    else:
        print("No existe")

def eliminar_materia(data):
    stu = data["estudiantes"]
    doc = input("Ingresa tu documento: ")
    if doc in stu:
        materia = input("Nombre de la materia a eliminar: ")
        if materia in stu[doc]["materias"]:
            stu[doc]["materias"].pop(materia)
            print(f"Materia {materia} eliminada con éxito.")
        else:
            print(f"La materia {materia} no existe para el estudiante con documento {doc}.")
    else:
        print("El estudiante no existe!")

def mostrar_estudiantes(data):
    for doc, info in data["estudiantes"].items():
        nombre = info["nombre"]
        materias = ", ".join(info["materias"].keys())
        print(f'Numero de documento: {doc}, Nombre: {nombre}, Materias: {materias}')

menu = ("1. Agregar estudiantes", "2. Agregar materia a estudiante existente", 
        "3. Actualizar nota de estudiante en una materia", "4. Eliminar materia", 
        "5. Mostrar estudiantes", "6. Mostrar todo", "0. Salir")

escuela = {
    "estudiantes" : {
        "123456": {
            "nombre" : "adrian",
            "materias" : {
                "biologia" : {
                    "trimestre 1" : 90,
                    "trimestre 2" : 100,
                    "trimestre 3" : 80
                }
                
            }
        }
    }
}

while True:
    for i in menu:
        print(i)
    opt = int(input("Ingresa una opcion: "))
    if opt == 0:
        print("Adios...")
        break
    elif opt == 1:
        registrar_estudiante(escuela)
    elif opt == 2:
        añadir_materia(escuela)
    elif opt == 3:
        actualizar_nota(escuela)
    elif opt == 4:
        eliminar_materia(escuela)
    elif opt == 5:
        mostrar_estudiantes(escuela)
    elif opt == 6:
        print(escuela["estudiantes"])