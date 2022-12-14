# Regla de Sarrus 3x3 con bucles, es decir, de manera iterativa y recursiva, es decir, de manera recursiva

def submatriz(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinante(matriz):
    if len(matriz) != len(matriz[0]):
        return 'Matriz no cuadrada'
    else:
        if(len(matriz) == 2):
            valor = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]
            return valor
        suma = 0
        for columna_actual in range(len(matriz)):
            signo = (-1) ** (columna_actual)
            sub_det = determinante(submatriz(matriz, 0, columna_actual))
            suma += (signo * matriz[0][columna_actual] * sub_det)
        return suma