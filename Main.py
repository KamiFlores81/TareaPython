import datetime
from ArbolBinario import *


class Persona:
    def __init__(self, nombre, fechaNacimiento):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
    def edad(self):
        hoy = datetime.date.today()
        return hoy.year - self.fechaNacimiento.year
    def __str__(self):
        return self.nombre + "(" + str(self.edad()) + ") [" + self.fechaNacimiento.strftime("%d-%m-%Y") + "]"
        
arbol = ArbolBinario(Persona("Elisa", datetime.date(1981,12,13)), lambda x,y: x.fechaNacimiento > y.fechaNacimiento)
agregarElemento(arbol, Persona("Yesi", datetime.date(1984,12,1)))
agregarElemento(arbol, Persona("Leo", datetime.date(1980,11,1)))
agregarElemento(arbol, Persona("Pablo", datetime.date(1978,8,13)))
agregarElemento(arbol, Persona("Javier", datetime.date(1982,4,29)))
agregarElemento(arbol, Persona("Azul", datetime.date(2011,11,2)))
agregarElemento(arbol, Persona("Zoe", datetime.date(2007,6,4)))

def imprimir(elemento):
    print (elemento)

print ("in-orden:")
print ("-" * 40)
ejecutarInOrden(arbol, imprimir)

print ("\npre-orden")
print ("-" * 40)
ejecutarPreOrden(arbol, imprimir)

print ("\npost-orden")
print ("-" * 40)
ejecutarPostOrden(arbol, imprimir)

