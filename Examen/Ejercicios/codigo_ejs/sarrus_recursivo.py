# Regla de Sarrus 3x3 llamándose a si mismo, es decir, de manera recursiva

def submatriz(matriz, c):
    B = [[1] * len(matriz) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            B[i][j] = matriz[i][j]
    B.pop(0)

    for i in range(len(B)):
        B[i].pop(c)
    return B

def determinante_recur(matriz):
    X = 0
    if len(matriz) != len(matriz[0]):
        print('Matriz no cuadrada')
    else:
        if len(matriz) <= 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        else:
            for i in range(len(matriz)):
                X = X + ((-1) ** (i)) * matriz[0][i] * determinante_recur(submatriz(matriz, i))
    return X