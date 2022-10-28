# Regla de Sarrus 3x3 con bucles, es decir, de manera iterativa

def factor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinante(matriz):
    if(len(matriz) == 2):
        valor = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]
        return valor
    suma = 0
    for columna_actual in range(len(matriz)):
        signo = (-1) ** (columna_actual)
        sub_det = determinante(factor(matriz, 0, columna_actual))
        suma += (signo * matriz[0][columna_actual] * sub_det)
    return suma

if __name__ == '__main__':
    matriz = [[1, 0, 2],
           [3, 0, 0],
           [2, 1, 4]]
    print('El determinante de la matriz es :', determinante(matriz))