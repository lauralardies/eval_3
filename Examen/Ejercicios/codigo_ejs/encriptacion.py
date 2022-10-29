def hash_encriptar(c):
    indice = ord(c) - 32
    if indice > 125 or indice < 0:
        return -1
    return indice

def hash_descencriptar(cadena):
    return ord(cadena[0] - 33)

def crear_tablas(encriptar, desencriptar):
    for i in range(33, 157):
        valor = ''
        for j in range(i, i + 8):
            valor = valor + chr(j)
        encriptar.append(valor)
        desencriptar.append(chr(i- 1))

encriptar = []
desencriptar = []
tablas = crear_tablas(encriptar, desencriptar)