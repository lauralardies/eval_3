from torres_hanoi import TorreHanoi
from sarrus_iterativo import determinante_iter

print('¿Qué ejercicio quiere resolver?')
print('-------------------------------')
print('EJERCICIO 1: TORRES DE HANOI')
print('EJERCICIO 2: REGLA DE SARRUS')
print('EJERCICIO 3: NAVES STAR WARS')
print('EJERCICIO 4: TDA POLINOMIO')
print('EJERCICIO 5: ALGORITMO DE ENCRIPTACIÓN')
seleccion = int(input('>> '))   

if seleccion == 1:
    TorreHanoi(64, 'A', 'B', 'C')
if seleccion == 2:
    matriz = [[1, 0, 2],
           [3, 0, 0],
           [2, 1, 4]]
    print('¿Quieres resolver el ejercicio de manera iterativa (1) o recursiva(2)?')
    opcion = int(input('>> '))   
    if opcion == 1:
        print('El determinante de la matriz es :', determinante_iter(matriz))