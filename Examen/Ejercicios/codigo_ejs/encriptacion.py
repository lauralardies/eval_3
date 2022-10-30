def hash_encriptar(c): 
    indice = ord(c) - 32
    if indice > 93 or indice < 0: # Si el caracter no se encuentra entre el 32 y 125 de la tabla ASCII, devolvemos -1
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
        m = hash_encriptar(mensaje[i])
        if m == -1: # En el caso en el que hayamos introducido un caracter no válido
            print('Ignorando el carácter ', mensaje[i])
        else:
            d.append(encriptacion[hash_encriptar(mensaje[i])])
    return ''.join(d) # Transformamos la lista en string

def desencriptar(mensaje, desencriptacion):
    d = []
    for i in range(0, len(mensaje), 8): # Vamos de 8 en 8 porque cada caracter se encripta como 8 caracteres
        d.append(desencriptacion[hash_descencriptar(mensaje[i])])
    return ''.join(d) # Transformamos la lista en string