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
    agregar_nave_nombre(coleccion, nave)
    agregar_nave_largo(coleccion, nave)

def agregar_nave_nombre(coleccion, nave):
    if coleccion.nombre == None:
        coleccion.nombre = nave.nombre
    else:
        act = coleccion.nombre
        ant = act
        while act.sig != None and act.info < nave.nombre.info:
            ant = act
            act = act.sig
        if coleccion.nombre == act and act.info > nave.nombre.info:
            nave.nombre.sig = act
            coleccion.nombre = nave.nombre
        else:
            if act.info < nave.nombre.info:
                nave.nombre.sig = act.sig
                act.sig = nave.nombre
            else:
                nave.nombre.sig = ant.sig
                ant.sig = nave.nombre

def agregar_nave_largo(coleccion, nave):
    if coleccion.largo == None:
        coleccion.largo = nave.largo
    else:
        act = coleccion.largo
        ant = act
        while act.sig != None and act.info > nave.largo.info:
            ant = act
            act = act.sig
        if coleccion.largo == act and act.info < nave.largo.info:
            nave.largo.sig = act
            coleccion.largo = nave.largo
        else:
            if act.info > nave.largo.info:
                nave.largo.sig = act.sig
                act.sig = nave.largo
            else:
                nave.largo.sig = ant.sig
                ant.sig = nave.largo

def mostrar_naves_nombre(coleccion):
    aux = coleccion.nombre
    while aux != None:
        nave = aux.parent
        print('La nave', nave.nombre.info, 'con', nave.largo.info, 'metros de largo. La tripulación es de', nave.tripulacion.info, 'personas y caben', nave.pasajeros.info, 'pasajeros')
        aux = aux.sig

def mostrar_naves_largo(coleccion):
    aux = coleccion.largo
    while aux != None:
        nave = aux.parent
        print('La nave', nave.nombre.info, 'con', nave.largo.info, 'metros de largo. La tripulación es de', nave.tripulacion.info, 'personas y caben', nave.pasajeros.info, 'pasajeros')
        aux = aux.sig
    
    
coleccion = Naves()
agregar_nave(coleccion, Nave('H',1,2,3))
agregar_nave(coleccion, Nave('J',2,4,5))
agregar_nave(coleccion, Nave('A',7,4,5))
agregar_nave(coleccion, Nave('M',3,4,5))
agregar_nave(coleccion, Nave('B',5,7,0))

mostrar_naves_nombre(coleccion)
print('')
mostrar_naves_largo(coleccion)