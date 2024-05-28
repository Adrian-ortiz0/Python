#Una universidad está organizando las inscripciones para los cursos del semestre de otoño. Por lo tanto requiere un programa que:
#Permita registrar a los estudiantes en los cursos del semestre pidiendo: matrícula, nombre, edad y carrera.
#Permita registrar los cursos pidiendo: nombre del curso, profesor y día de la semana.
#Permita quitar del registro a los estudiantes.
#Permita eliminar y/o modificar cursos.
#Para inscribirse en los cursos, los estudiantes deben pagar una cuota de 200.000 COP. Por lo tanto el programa también debe:

#Saber cuántos estudiantes no han pagado aún la cuota y cuánto dinero suma la deuda.
#Saber cuáles estudiantes (listarlos) no han pagado.
#No permitir quitar del registro a estudiantes que ya hayan pagado, pues no se aceptan devoluciones.
#Marcar cursos ya realizados.
#No permitir eliminar o modificar cursos ya realizados.
#Aspectos a tener en cuenta:

#La estructura a utilizar es libre, solo se pide que sea ordenada y coherente.
#Todo debe ser dentro de un menú que se repite para no perder la información y al presionar la opción de salida se debe pedir confirmación de la misma.

semestre = {
    "estudiantes" : {
        "15784935" : {
            "Nombre" : "adrian",
            "Edad" : 22,
            "Carrera" : "sistemas",
            "Pago_realizado" : False,
            "Cursos" : []
        }
    },
    "cursos" : {
        "Poo" : {
            "profesor" : "eloy",
            "dia" : "viernes"
        }        
    }
}

def registrar_estudiantes(dic):
    estudiante = {}
    matricula = input("Ingresa la matricula: ")
    if dic["estudiantes"].get(matricula, None) == None:
        estudiante["Nombre"] = input("Ingresa el nombre: ")
        estudiante["Edad"] = int(input("Ingresa edad: "))
        estudiante["Carrera"] = input("Ingresa la carrera: ")
        estudiante["Pago_realizado"] = False
        estudiante["Cursos"] = []
        dic["estudiantes"][matricula] = estudiante
        print(estudiante)
    else:
        print("estudiante ya existe!")

def registrar_cursos(dic):
    curso = {}
    nombre_curso = input("Ingresa el nombre del curso: ")
    if dic["cursos"].get(nombre_curso, None) == None:
        curso["profesor"] = input("Nombre del profesor: ")
        curso["dia"] = input("Nombre del dia: ")
        dic["cursos"][nombre_curso] = curso
        print(curso)
    else:
        print("El curso ya existe!")

def modificar_cursos(dic):
    cursos = dic["cursos"]
    print(cursos)
    cur = input("Curso que desea modificar: ")
    cursos[cur]["profesor"] = input("Nuevo profesor: ")
    cursos[cur]["dia"] = input("Nuevo dia: ")
    print(cursos[cur])

def pagar_estudiante(dic):
    estudiantes = dic["estudiantes"]
    print(estudiantes)
    doc = input("Documento del usuario a pagar: ")
    if dic["estudiantes"].get(doc, None) != None:
        dic["estudiantes"][doc]["Pago_realizado"] = True
        print(estudiantes)
    else:
        print("No existe ese documento")

def agregar_cursos_estudiantes(dic):
    estudiantes = dic["estudiantes"]
    cursos = dic["cursos"]
    print(estudiantes)
    doc = input("Documento del usuario a agregar cursos: ")
    if dic["estudiantes"].get(doc, None) != None:
        print(cursos)
        curs = input("Ingresa el nombre del curso a inscribir: ")
        dic["estudiantes"][doc]["Cursos"].append(curs)
        print(f"Curso agregado con exito!")
    
        
menu = ("1. Registrar estudiantes","2. Registrar cursos", "3. Mostrar estudiantes", "4. Mostrar cursos", 
        "5. Modificar curso", "6. Pagar estudiante", "0. Salir")

while True:
    for i in menu:
        print(i)
    inp = int(input("Type option: "))
    if inp == 0:
        print("Saliendo...")
        break
    elif inp == 1:
        registrar_estudiantes(semestre)
    elif inp == 2:
        registrar_cursos(semestre)
    elif inp == 3:
        print(semestre["estudiantes"])
    elif inp == 4:
        print(semestre["cursos"])
    elif inp == 5:
        modificar_cursos(semestre)
    elif inp == 6:
        pagar_estudiante(semestre)
    elif inp == 7:
        agregar_cursos_estudiantes(semestre)