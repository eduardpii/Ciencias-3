class Moto_estudiante:
    def __init__(self):
        nombre = ""
        codigo = ""
        placa = ""

    def __init__(self, nombre, codigo, placa):
        self.nombre = nombre
        self.codigo = codigo
        self.placa = placa

    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setPlaca(self, placa):
        self.placa = placa

    def getNombre(self):
        return self.nombre
    
    def getCodigo(self):
        return self.codigo
    
    def getPlaca(self):
        return self.placa
