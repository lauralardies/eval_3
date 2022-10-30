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
        if aux.info.termino == actual.info.termino: # Si el término ya existe en nuestro polinomio, en vez de crear otro término nuevo, sumo sus valores.
            actual.info.valor = actual.info.valor + aux.info.valor
        else:
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

def multiplicar(polinomio1, polinomio2):
    paux = Polinomio()
    pol1 = polinomio1.termino_mayor
    while pol1 is not None:
        pol2 = polinomio2.termino_mayor
        while pol2 is not None:
            termino = pol1.info.termino + pol2.info.termino
            valor = pol1.info.valor * pol2.info.valor
            if obtener_valor(paux, termino) != 0:
                valor += obtener_valor(paux, termino)
                modificar_termino(paux, termino, valor)
            else:
                agregar_termino(paux, termino, valor)
            pol2 = pol2.sig
        pol1 = pol1.sig
    return paux

# Ahora comenzamos con el ejercicio, primero realizamos la función de RESTAR 
def restar(polinomio1, polinomio2):
    paux = Polinomio()
    mayor = polinomio1 if polinomio1.grado >= polinomio2.grado else polinomio2
    menor = polinomio2 if polinomio1 == mayor else polinomio1
    print('\nEstamos haciendo la resta', mostrar(mayor), '-', mostrar(menor))
    for i in range(0, mayor.grado + 1):
        total = obtener_valor(mayor, i) - obtener_valor(menor, i)
        if total != 0:
            agregar_termino(paux, i, total)
    return paux

# Seguimos con la función de DIVIDIR
def dividir(polinomio1, polinomio2, paux):
    a = polinomio1.termino_mayor
    b = polinomio2.termino_mayor
    c = Polinomio()
    termino = a.info.termino - b.info.termino
    valor = a.info.valor / b.info.valor
    agregar_termino(paux, termino, valor)
    agregar_termino(c, termino, valor)
    m = multiplicar(polinomio2, c)
    resto = restar(polinomio1, m)
    if resto.grado >= polinomio2.grado:
        return dividir(resto, polinomio2, paux)
    else:
        if resto.grado == -1:
            agregar_termino(resto, 0, 0)
        return paux, resto

# La siguiente función a realizar es ELIMINAR un polinomio
def eliminar(polinomio, termino):
    if termino > polinomio.grado: # El término a buscar no está en el polinomio al ser más grande
        return polinomio
    else:
        actual = polinomio.termino_mayor
        anterior = polinomio.termino_mayor
        while actual.sig is not None and termino < actual.info.termino:
            anterior = actual
            actual = actual.sig
        if actual == anterior: # Actualizamos el término mayor y el grado del polinomio si el término que queremos quitar es el primero
            polinomio.termino_mayor = actual.sig
            polinomio.grado = actual.info.termino
        else:
            if termino == actual.info.termino:
                anterior.sig = actual.sig
        return polinomio

# Ahora vamos a ver si el término BUSCADO se encuentra en nuestro polinomio
def buscar(polinomio, termino):
    if obtener_valor(polinomio, termino) == 0: # Si no se puede obtener el valor del término buscado , significa que el término no se encuentra en el polinomio
        return('El término {} no se encuentra en nuestro polinomio'.format(termino))
    else:
        return('El término {} sí se encuentra en nuestro polinomio'.format(termino))
