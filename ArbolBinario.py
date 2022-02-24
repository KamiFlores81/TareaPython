
class ArbolBinario:
    def __init__(self, elemento, esMenorFunction = lambda x,y: x < y):
        self.derecha = None
        self.izquierda = None
        self.elemento = elemento
        self.esMenor = esMenorFunction

def profundidad(arbol):
    if arbol == None:
        return 0       
    return 1 + maximaProfundidadDeHijo(arbol)

def maximaProfundidadDeHijo(arbol):
    return max([profundidad(arbol.izquierda), profundidad(arbol.derecha)])
 
def agregarElemento(arbol, elemento):
    if arbol.esMenor(elemento, arbol.elemento):
        agregarIzquierda(arbol, elemento)      
    else:
        agregarDerecha(arbol, elemento)
                                              
def agregarIzquierda(arbol, elemento):
    if arbol.izquierda == None:
        arbol.izquierda = ArbolBinario(elemento, arbol.esMenor)
    else:
        agregarElemento(arbol.izquierda, elemento)
        
def agregarDerecha(arbol, elemento):
    if arbol.derecha == None:
        arbol.derecha = ArbolBinario(elemento, arbol.esMenor)
    else:
        agregarElemento(arbol.derecha, elemento)

#
#
# RECORRIDOS
#        
#

def ejecutarPreOrden(arbol, funcion):
    if (arbol != None):
        funcion(arbol.elemento)
        ejecutarPreOrden(arbol.izquierda, funcion)
        ejecutarPreOrden(arbol.derecha, funcion)
        
def ejecutarInOrden(arbol, funcion):
    if (arbol == None):
        return
    ejecutarInOrden(arbol.izquierda, funcion)
    funcion(arbol.elemento)
    ejecutarInOrden(arbol.derecha, funcion)

def ejecutarPostOrden(arbol, funcion):
    if (arbol != None):
        ejecutarPostOrden(arbol.izquierda, funcion)
        ejecutarPostOrden(arbol.derecha, funcion)
        funcion(arbol.elemento)

