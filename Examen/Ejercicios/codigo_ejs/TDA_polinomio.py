# Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
# restar
# dividir
# eliminar un término
# determinar si un término existe en un polinomio


# Comenzamos mostrando las funciones para crear el polinomio

class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

def agregar_termino(polinomio, termino, valor):
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if termino > polinomio.grado:
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        while actual.sig is not None and termino < actual.sig.info.termino:
            actual = actual.sig
        aux.sig = actual.sig
        actual.sig = aux

polinomio = Polinomio()
