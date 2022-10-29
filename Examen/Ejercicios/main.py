import unittest
from codigo_ejs.torres_hanoi import TorreHanoi
from codigo_ejs.sarrus_iterativo import determinante_iter
from codigo_ejs.sarrus_recursivo import determinante_recur
from codigo_ejs.TDA_polinomio import Polinomio, agregar_termino, mostrar, restar, dividir, eliminar, buscar

print('¿Qué ejercicio quiere resolver?')
print('-------------------------------')
print('EJERCICIO 1: TORRES DE HANOI')
print('EJERCICIO 2: REGLA DE SARRUS')
print('EJERCICIO 3: NAVES STAR WARS')
print('EJERCICIO 4: TDA POLINOMIO')
print('EJERCICIO 5: ALGORITMO DE ENCRIPTACIÓN')
print('-------------------------------')
seleccion = int(input('>> '))   

if seleccion == 1:
    # El problema se acaba resolviendo pero debido al alto tiempo de ejecución, no se puede comprobar.
    # Si la Torre de Hanoi tiene n-discos sería necesario realizar (2^n)-1 movimientos.
    TorreHanoi(64, 'A', 'C', 'B')
elif seleccion == 2:
    matriz = [[1, 0, 2],
           [3, 0, 0],
           [2, 1, 4]]
    print('¿Quieres resolver el ejercicio de manera iterativa (1) o recursiva(2)?')
    opcion = int(input('>> '))   
    if opcion == 1:
        print('El determinante de la matriz es :', determinante_iter(matriz))
    if opcion == 2:
        print('El determinante de la matriz es :', determinante_recur(matriz))
    unittest.main()

elif seleccion == 3:
    print('Este ejercicio no está hecho')

elif seleccion == 4:
    polinomio1 = Polinomio()
    agregar_termino(polinomio1, 1, 2)
    agregar_termino(polinomio1, 2, 3)
    agregar_termino(polinomio1, 0, 5)

    polinomio2 = Polinomio()
    agregar_termino(polinomio2, 1, 3)
    agregar_termino(polinomio2, 2, -1)

    print('Mi primer polinomio es ', mostrar(polinomio1))
    print('Mi segundo polinomio es ', mostrar(polinomio2))
    
    print('¿Quiere restar el polinomio (1), dividirlo (2), eliminar un término (3) o determinar si existe un término en el polinomio(4)?')
    opcion = int(input('>> ')) 
    if opcion == 1:
        print('La resta de los polinomios es ', mostrar(restar(polinomio1, polinomio2)))
    if opcion == 2:
        print('La división de polinomios es ', mostrar(dividir(polinomio1, polinomio2)))
    if opcion == 3:
        print('Se ha eliminado el término, el polinomio resultante es ', mostrar(eliminar(polinomio1, 1)))
    if opcion == 4:
        buscar(polinomio1, 3)

elif seleccion == 5:
    print('Este ejercicio no está hecho')

else:
    print('No has seleccionado un número de ejercicio válido')