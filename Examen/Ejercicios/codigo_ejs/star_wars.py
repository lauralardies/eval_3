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

def mostrar_nave(nave):
    sol = 'La nave {} con {} metro(s) de largo. La tripulaci??n es de {} persona(s) y caben {} pasajero(s)'.format(nave.nombre.info, nave.largo.info, nave.tripulacion.info, nave.pasajeros.info)
    return sol

def mostrar_naves(coleccion):
    aux = coleccion
    while aux != None:
        nave = aux.parent
        print(mostrar_nave(nave))
        aux = aux.sig