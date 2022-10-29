class Nodo(object):
    def __init__(self, info):
        self.info = info
        self.sig = None
        

class Nave(object):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = Nodo(nombre)
        self.largo = Nodo(largo)
        self.tripulacion = Nodo(tripulacion)
        self.pasajeros = Nodo(pasajeros)
        
class Naves(object):
    nombre, largo, tripulacion, pasajeros = None, None, None, None

def agregar_nave(coleccion, nave):
    if coleccion.nombre == None:
        coleccion.nombre = nave.nombre
    else:
        aux = coleccion.nombre
        while aux.sig != None and aux.info < nave.nombre.info:
            aux = aux.sig
        if coleccion.nombre == aux and aux.sig != None:
            nave.nombre.sig = aux
            coleccion.nombre = nave.nombre
        else:
            nave.nombre.sig = aux.sig
            aux.sig = nave.nombre
    
coleccion = Naves()
agregar_nave(coleccion, Nave('H',1,2,3))
agregar_nave(coleccion, Nave('J',3,4,5))
agregar_nave(coleccion, Nave('A',3,4,5))
agregar_nave(coleccion, Nave('M',3,4,5))

print(coleccion)