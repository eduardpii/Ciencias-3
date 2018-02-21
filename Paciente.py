class Paciente:
    def __init__(self):
        nombre = ""
        cedula = ""
        especialidad = ""

    def __init__(self, nombre, cedula, especialidad):
        self.nombre = nombre
        self.cedula = cedula
        self.especialidad = especialidad

    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setCedula(self, cedula):
        self.cedula = cedula

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def getNombre(self):
        return self.nombre
    
    def getCedula(self):
        return self.cedula
    
    def getEspecialidad(self):
        return self.especialidad
