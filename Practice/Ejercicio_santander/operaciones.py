import ciclismo
import atletismo
import patinaje
from menu import *

def op():
    while True:
        menu
        opt = int(input("Ingresa una opciòn: "))
        
        if opt == 0:
            print("Adios...")
            break
        elif opt == 1:
            ciclismo.registrar_usuarios(ciclismo.participantes_ciclismo)
        elif opt == 2:
            atletismo.registrar_usuarios(atletismo.participantes_atletismo)
        elif opt == 3:
            patinaje.registrar_usuarios(patinaje.participantes_patinaje)
        elif opt == 4:
            ciclismo.mostrar_usuarios(ciclismo.participantes_ciclismo)
        elif opt == 5:
            atletismo.mostrar_usuarios(atletismo.participantes_atletismo)
        elif opt == 6:
            patinaje.mostrar_usuarios(patinaje.participantes_patinaje)
        elif opt == 7:
            patinaje.ranking(patinaje.participantes_patinaje)