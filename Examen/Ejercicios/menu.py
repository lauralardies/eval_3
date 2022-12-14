from codigo_ejs.torres_hanoi import TorreHanoi
from codigo_ejs.sarrus import determinante
from codigo_ejs.star_wars import Naves, Nave, agregar_nave, mostrar_naves, mostrar_nave
from codigo_ejs.TDA_polinomio import Polinomio, agregar_termino, mostrar, restar, dividir, eliminar, buscar
from codigo_ejs.encriptacion import crear_tablas, encriptar, desencriptar

while True:

    print('¿Qué ejercicio quieres resolver?')
    print('-------------------------------')
    print('EJERCICIO 1: TORRES DE HANOI')
    print('EJERCICIO 2: REGLA DE SARRUS')
    print('EJERCICIO 3: NAVES STAR WARS')
    print('EJERCICIO 4: TDA POLINOMIO')
    print('EJERCICIO 5: ALGORITMO DE ENCRIPTACIÓN')
    print('OPCIÓN 6: SALIR')
    print('-------------------------------')
    seleccion = input('>> ')

    if seleccion == '1':
        # El problema se acaba resolviendo pero debido al alto tiempo de ejecución, no se puede comprobar.
        # Si la Torre de Hanoi tiene n-discos sería necesario realizar (2^n)-1 movimientos.
        TorreHanoi(74, 'A', 'C', 'B')

    elif seleccion == '2':
        matriz = [[1, 0, 2],
            [3, 0, 0],
            [2, 1, 4]]
        print('Mi matriz es la siguiente:')
        for i in range(len(matriz)):
            print(matriz[0][i], matriz[1][i], matriz[2][i])
        print('El determinante de la matriz es :', determinante(matriz))
        
    elif seleccion == '3':
        coleccion = Naves()
        agregar_nave(coleccion, Nave('Halcón Milenario', 34.37, 4, 3))
        agregar_nave(coleccion, Nave('Estrella de la Muerte', 120000, 256, 16000))
        agregar_nave(coleccion, Nave('Ala-X', 12.5, 1, 0))
        agregar_nave(coleccion, Nave('Destructor Estelar', 1600, 46700, 0))
        agregar_nave(coleccion, Nave('AT-ST', 8.6, 2, 0))
        agregar_nave(coleccion, Nave('AT-AT', 44, 3, 40))
        agregar_nave(coleccion, Nave('AT-ET', 13.2, 7, 38))
        agregar_nave(coleccion, Nave('Droide Buitre', 3.6, 1, 0))
        agregar_nave(coleccion, Nave('Caza Estelar N-1', 11, 2, 0))
        agregar_nave(coleccion, Nave('Esclavo I', 21.5, 3, 2))
        agregar_nave(coleccion, Nave('Nave de asalto clase Acclamator', 752, 700, 16000))
        agregar_nave(coleccion, Nave('Cañonera LAAT', 28.8, 6, 30))
        agregar_nave(coleccion, Nave('Caza Estelar V-19 Torrente', 6, 1, 0))
        agregar_nave(coleccion, Nave('Tantive IV', 126.68, 3, 100))
        agregar_nave(coleccion, Nave('Desalmado Uno', 6.71, 1, 0))
        agregar_nave(coleccion, Nave('Espíritu', 43.9, 1, 6))
        agregar_nave(coleccion, Nave('Caza TIE', 6.3, 1, 0))

        print('¿Qué quieres hacer?')
        print('1 - Realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente')
        print('2 - Mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”')
        print('3 - Determinar cuáles son las cinco naves con mayor cantidad de pasajeros')
        print('4 - Indicar cuál es la nave que requiere mayor cantidad de tripulación')
        print('5 - Mostrar todas las naves que comienzan con AT')
        print('6 - Listar todas las naves que pueden llevar seis o más pasajeros')
        print('7 - Mostrar toda la información de la nave más pequeña y la más grande')
        opcion = input('>> ')

        if opcion == '1':
            print('\nLas naves ordenadas por nombre de manera ascendente')
            mostrar_naves(coleccion.nombre) 
            print('\nLas naves ordenadas por largo de manera descendente')
            mostrar_naves(coleccion.largo)

        elif opcion == '2':
            print('\nLa información del “Halcón Milenario” y la “Estrella de la Muerte” es la siguiente:')
            lista = coleccion.nombre
            while lista != None:
                nave = lista.parent
                if lista.info == 'Halcón Milenario' or lista.info == 'Estrella de la Muerte':
                    print(mostrar_nave(nave))
                lista = lista.sig

        elif opcion == '3':
            print('\nLas cinco naves con mayor cantidad de pasajeros son:')
            lista = coleccion.pasajeros
            for i in range(0, 5):
                nave = lista.parent
                print(mostrar_nave(nave))
                lista = lista.sig
                if lista == None:
                    break

        elif opcion == '4':
            lista = coleccion.tripulacion
            nave = lista.parent
            print('\nLa nave que requiere más cantidad de tripulación es:')
            print(mostrar_nave(nave))
        
        elif opcion == '5':
            print('\nLas naves que empiezan con “AT” son las siguientes:')
            lista = coleccion.nombre
            while lista != None:
                nave = lista.parent
                if lista.info.startswith('AT'):
                    print(mostrar_nave(nave))
                lista = lista.sig

        elif opcion == '6':
            print('\nLas naves que pueden llevar 6 pasajeros o más son:')
            lista = coleccion.pasajeros
            while lista != None:
                nave = lista.parent
                if lista.info >= 6:
                    print(mostrar_nave(nave))
                lista = lista.sig
        
        elif opcion == '7':
            print('\nLa información de la nave más grande y más pequeña es:')
            lista = coleccion.largo
            nave = lista.parent
            print(mostrar_nave(nave))
            while lista.sig != None:
                lista = lista.sig
                nave = lista.parent
            print(mostrar_nave(nave))

        else:
            print('\nNo has seleccionado un número de ejercicio válido')
    
    elif seleccion == '4':
        polinomio1 = Polinomio()
        agregar_termino(polinomio1, 4, 1)
        agregar_termino(polinomio1, 1, 1)
        agregar_termino(polinomio1, 0, 1)

        polinomio2 = Polinomio()
        agregar_termino(polinomio2, 2, 1)
        agregar_termino(polinomio2, 0, 1)

        print('Mi primer polinomio es ', mostrar(polinomio1))
        print('Mi segundo polinomio es ', mostrar(polinomio2))

        print('¿Quiere restar el polinomio (1), dividirlo (2), eliminar un término del primer polinomio (3) o determinar si existe un término en el primer polinomio (4)?')
        opcion = input('>> ')

        if opcion == '1':
            print('La resta de los polinomios es', mostrar(restar(polinomio1, polinomio2)))

        elif opcion == '2':
            paux = Polinomio()
            cociente, resto = dividir(polinomio1, polinomio2, paux)
            print('\nLa división de polinomios es', mostrar(cociente), 'con resto', mostrar(resto))

        elif opcion == '3':
            print('¿Qué polinomio quieres modificar? Polinomio 1 (1); Polinomio 2 (2)')
            eleccion1 = input('>> ')
            print('¿Qué termino quieres eliminar?')
            eleccion2 = input('>> ')
            try:
                eleccion1 = int(eleccion1)
                eleccion2 = int(eleccion2)
                if eleccion1 == 1:
                    eleccion1 = polinomio1
                elif eleccion1 == 2:
                    eleccion1 = polinomio2
                else:
                    print('Tienes que seleccionar un polinomio válido')
                    exit()
                print('\nSe ha eliminado el término {}, el polinomio resultante es{}'.format(eleccion2, mostrar(eliminar(eleccion1, eleccion2))))
            
            except ValueError:
                print('Debes introducir un número')

        elif opcion == '4':
            print('¿Qué polinomio quieres analizar? Polinomio 1 (1); Polinomio 2 (2)')
            eleccion1 = input('>> ')
            print('¿Qué termino quieres buscar?')
            eleccion2 = input('>> ')
            try:
                eleccion1 = int(eleccion1)
                eleccion2 = int(eleccion2)
                if eleccion1 == 1:
                    eleccion1 = polinomio1
                elif eleccion1 == 2:
                    eleccion1 = polinomio2
                else:
                    print('Tienes que seleccionar un polinomio válido')
                    exit()
                print('\n', buscar(eleccion1, eleccion2))

            except  ValueError:
                print('Debe introducir un número')

        else:
            print('\nNo has seleccionado un número de ejercicio válido')

    elif seleccion == '5':
        encriptacion, desencriptacion = crear_tablas()
        print('\n¿Qué mensaje deseas encriptar?')
        mensaje = input('>> ')

        print('Mensaje encriptado: ', encriptar(mensaje, encriptacion))
        print('\n¿Quieres desencriptar el mensaje? Si(1); No(2)')
        opcion = input('>> ')

        if opcion == '1':
            print('Mensaje desencriptado: ', desencriptar(encriptar(mensaje, encriptacion), desencriptacion))

    elif seleccion == '6':
        break

    else:
        print('\nNo has seleccionado un número de ejercicio válido')
    
    print('\n¿Quieres resolver algún ejercicio más? Sí(1); No(2)')
    opcion = input('>> ')

    if opcion == '2':
        break