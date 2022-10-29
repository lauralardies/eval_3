def hash_encriptar(c):
    indice = ord(c) - 32
    if indice > 125 or indice < 0:
        return -1
    return indice

def hash_descencriptar(c):
    return ord(c[0]) - 33

def crear_tablas():
    encriptacion = []
    desencriptacion = []
    for i in range(33, 157):
        valor = ''
        for j in range(i, i + 8):
            valor = valor + chr(j)
        encriptacion.append(valor)
        desencriptacion.append(chr(i- 1))
    return encriptacion, desencriptacion

def encriptar(mensaje, encriptacion):
    d = []
    for i in range(len(mensaje)):
        d.append(encriptacion[hash_encriptar(mensaje[i])])
    return ''.join(d)

def desencriptar(mensaje, desencriptacion):
    d = []
    for i in range(0, len(mensaje), 8):
        d.append(desencriptacion[hash_descencriptar(mensaje[i])])
    return ''.join(d)