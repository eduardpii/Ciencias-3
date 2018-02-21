from Paciente import *
from Cola import *
cardiologia = Cola()
pediatria=Cola()
geriatria=Cola()
def organizarPacientes(paciente):
    if(paciente.especialidad=="c"):
        cardiologia.encolar(paciente)
    elif(paciente.especialidad=="p"):
        pediatria.encolar(paciente)
    else:
        geriatria.encolar(paciente)

def mostrarLista(Cola):
    if(Cola.es_vacia()):
        return
    else:
        print(Cola.desencolar().nombre +" , "+ Cola.desencolar().cedula)
        mostrarLista(Cola)
        
    

def main():
    
    
    
    paciente1 = Paciente("Gomez", "20142020030","c")
    paciente2 = Paciente("Felipe", "20142020031","p")
    paciente3 = Paciente("Miguel", "20142020032","g")
    paciente4 = Paciente("Angel", "20142020033","g")
    paciente5 = Paciente("Neider", "20142020034","c")
    paciente6 = Paciente("Alejandro", "20142020035","c")
    paciente7 = Paciente("Cristian", "20142020036","p")
    paciente8 = Paciente("Camilo", "20142020037","g")
    paciente9 = Paciente("Camila", "20142020038","c")
    paciente10 = Paciente("Maria", "20142020039","p")
        
    
    organizarPacientes(paciente1)
    organizarPacientes(paciente2)
    organizarPacientes(paciente3)
    organizarPacientes(paciente4)
    organizarPacientes(paciente5)
    organizarPacientes(paciente6)
    organizarPacientes(paciente7)
    organizarPacientes(paciente8)
    organizarPacientes(paciente9)
    organizarPacientes(paciente10)
    print("Cardiologia")
    mostrarLista(cardiologia)
    print("Pediatria")
    mostrarLista(pediatria)
    print("Geriatria")
    mostrarLista(geriatria)

if __name__ == "__main__":
    main()

