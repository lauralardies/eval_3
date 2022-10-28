# Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
# restar
# dividir
# eliminar un término
# determinar si un término existe en un polinomio


# Comenzamos mostrando las funciones que nos definen el polinomio

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

def modificar_termino(polinomio, termino, valor):
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino != termino:
        aux = aux.sig
    aux.info.valor = valor

def obtener_valor(polinomio, termino):
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:
        aux = aux.sig
    if aux is not None and aux.info.termino == termino:
        return aux.info.valor
    else:
        return 0

def mostrar(polinomio):
    aux = polinomio.termino_mayor
    pol = ''
    if aux is not None:
        while aux is not None:
            signo = ' '
            if aux.info.valor >= 0:
                signo += '+'
            pol += signo + str(aux.info.valor) + 'x^' + str(aux.info.termino)
            aux = aux.sig
    return pol

# Ahora comenzamos con el ejercicio, primero realizamos la función de RESTAR 
def restar(polinomio1, polinomio2):
    paux = Polinomio()
    mayor = polinomio1 if polinomio1.grado > polinomio2.grado else polinomio2
    menor = polinomio2 if polinomio1 == mayor else polinomio1
    for i in range(0, mayor.grado + 1):
        total = obtener_valor(mayor, i) - obtener_valor(menor, i)
        if total != 0:
            agregar_termino(paux, i, total)
    return paux

# Seguimos con la función de DIVIDIR
def dividir(polinomio1, polinomio2):
    paux = Polinomio()
    pol1 = polinomio1.termino_mayor
    while pol1 is not None:
        pol2 = polinomio2.termino_mayor
        while pol2 is not None:
            termino = pol1.info.termino - pol2.info.termino
            valor = pol1.info.valor / pol2.info.valor
            if obtener_valor(paux, termino) != 0:
                valor += obtener_valor(paux, termino)
                modificar_termino(paux, termino, valor)
            else:
                agregar_termino(paux, termino, valor)
            pol2 = pol1.sig
        pol1 = pol1.sig
    return paux

# La siguiente función a realizar es eliminar un polinomio
def eliminar(polinomio, termino):
    aux = Nodo()
    borrar = datoPolinomio(obtener_valor(polinomio, termino), termino)
    aux.info = borrar
    if termino > polinomio.grado: # El término a buscar no está en el polinomio al ser más grande
        return polinomio
    else:
        actual = polinomio.termino_mayor
        while actual.sig is not None and termino < actual.sig.info.termino:
            actual = actual.sig
        actual = aux.sig
        return polinomio

# Ahora vamos a ver si el término buscado se encuentra en nuestro polinomio
def buscar(polinomio, termino):
    if obtener_valor(polinomio, termino) == 0:
        print('El término {} no se encuentra en nuestro polinomio'.format(termino))
    else:
        print('El término {} sí se encuentra en nuestro polinomio'.format(termino))
