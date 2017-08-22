# -*- coding: cp1252 -*-
class Colas:
    def __init__(self):
        self.lista_aceptados = []

    def apilar(self, item):
        self.lista_aceptados.append(item)

    def desapilar(self):
        try:
            return self.lista_aceptados.pop(0)
        except:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        if self.lista_aceptados == []:
            return "La cola esta vacia"
        else:
            return "La lista no esta vacia"
