def registrar_usuario(data):
    name = input("Ingresa nombre: ")
    age = int(input("Ingresa edad: "))
    department = input("Ingresa departamento: ")
    department.lower
    if age >= 18 and department == "santander":
        competencias = ("atletismo", "ciclismo", "patinaje")
        for i in competencias:
            print(i)
        opt = input("En que competencia desea inscribirse: ")  
        if opt in competencias:
            data[opt].append(name)
            print(data[opt])          
        else:
            print("No existe esa competencia!")
    else:
        print("Eres menor de 18 o eres de otro departamento!")

participantes = {
    "atletismo" : [],
    "ciclismo" : [],
    "patinaje" : []
}

registrar_usuario(participantes)