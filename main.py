from Moto_Estudiante import *
from Colas import *
import random 

def main():
    ## Cola de motos que serán aceptadas
    motos_aceptadas = Colas()
    ## Motos
    moto1 = Moto_estudiante("Gomez", "20142020030", "ABC123")
    moto2 = Moto_estudiante("Felipe", "20142020031", "ABC124")
    moto3 = Moto_estudiante("Miguel", "20142020032", "ABC125")
    moto4 = Moto_estudiante("Angel", "20142020033", "ABC126")
    moto5 = Moto_estudiante("Neider", "20142020034", "ABC127")
    moto6 = Moto_estudiante("Alejandro", "20142020035", "ABC128")
    moto7 = Moto_estudiante("Cristian", "20142020036", "ABC129")
    moto8 = Moto_estudiante("Camilo", "20142020037", "ABC131")
    moto9 = Moto_estudiante("Camila", "20142020038", "ABC132")
    moto10 = Moto_estudiante("Maria", "20142020039", "ABC133")
    ## Motos en cola para pedir cupo
    motos_aceptadas.apilar(moto1)
    motos_aceptadas.apilar(moto2)
    motos_aceptadas.apilar(moto3)
    motos_aceptadas.apilar(moto4)
    motos_aceptadas.apilar(moto5)
    motos_aceptadas.apilar(moto6)
    motos_aceptadas.apilar(moto7)
    motos_aceptadas.apilar(moto8)
    motos_aceptadas.apilar(moto9)
    motos_aceptadas.apilar(moto10)
    ## Numero de cupos
    cupos = random.randrange(10)
    print("Hay " + str(cupos) + " disponibles")
    ## Lista de aceptados
    motos_parqueadero = []
    ## Comprobar que esta vacia
    print(motos_aceptadas.es_vacia())
    ## Añade las motos aceptadas a una nueva lista desapilando la cola
    ## el numero de veces determinado por los cupos
    for i in range (cupos):
        motos_parqueadero.append(motos_aceptadas.desapilar())
    ## Compruebo los ingresados
    for i in range(len(motos_parqueadero)):
        print(motos_parqueadero[i].getNombre())

main()

