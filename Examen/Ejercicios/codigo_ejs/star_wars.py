class Nodo(object):
    def __init__(self, info, parent):
        self.info = info
        self.sig = None
        self.parent = parent

class Nave(object):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = Nodo(nombre, self)
        self.largo = Nodo(largo, self)
        self.tripulacion = Nodo(tripulacion, self)
        self.pasajeros = Nodo(pasajeros, self)

class Naves(object):
    nombre, largo, tripulacion, pasajeros = None, None, None, None

def agregar_nave(coleccion, nave):
    coleccion.nombre = agregar_nave_asc(coleccion.nombre, nave.nombre)
    coleccion.largo = agregar_nave_desc(coleccion.largo, nave.largo)
    coleccion.tripulacion = agregar_nave_desc(coleccion.tripulacion, nave.tripulacion)
    coleccion.pasajeros = agregar_nave_desc(coleccion.pasajeros, nave.pasajeros)

def agregar_nave_asc(item, elemento):
    if item == None:
        item = elemento
        primero = item
    else:
        primero = item
        act = item
        ant = act
        while act.sig != None and act.info < elemento.info:
            ant = act
            act = act.sig
        if item == act and act.info > elemento.info:
            elemento.sig = act
            item = elemento
            primero = item
        else:
            if act.info < elemento.info:
                elemento.sig = act.sig
                act.sig = elemento
            else:
                elemento.sig = ant.sig
                ant.sig = elemento
    return primero

def agregar_nave_desc(item, elemento):
    if item == None:
        item = elemento
        primero = item
    else:
        primero = item
        act = item
        ant = act
        while act.sig != None and act.info > elemento.info:
            ant = act
            act = act.sig
        if item == act and act.info < elemento.info:
            elemento.sig = act
            item = elemento
            primero = item
        else:
            if act.info > elemento.info:
                elemento.sig = act.sig
                act.sig = elemento
            else:
                elemento.sig = ant.sig
                ant.sig = elemento
    return primero

def mostrar_naves(coleccion):
    aux = coleccion
    while aux != None:
        nave = aux.parent
        print('La nave', nave.nombre.info, 'con', nave.largo.info, 'metros de largo. La tripulación es de', nave.tripulacion.info, 'personas y caben', nave.pasajeros.info, 'pasajeros')
        aux = aux.sig

coleccion = Naves()
agregar_nave(coleccion, Nave('Halcón Milenario', 34.37, 4, 3))
agregar_nave(coleccion, Nave('Estrella de la Muerte', 120000, 75, 226))
agregar_nave(coleccion, Nave('Ala-X', 12.5, 1, 0))
agregar_nave(coleccion, Nave('Destructor Estelar', 1600, 46700, 0))
agregar_nave(coleccion, Nave('AT-ST', 8.6, 2, 0))
agregar_nave(coleccion, Nave('AT-AT', 44, 3, 40))
agregar_nave(coleccion, Nave('AT-ET', 13.2, 7, 38))

mostrar_naves(coleccion.nombre)
print('')
mostrar_naves(coleccion.largo)
print('')
mostrar_naves(coleccion.tripulacion)
print('')
mostrar_naves(coleccion.pasajeros)
print('')