import unittest
from star_wars import Naves, Nave, agregar_nave, mostrar_nave

class TestNaves(unittest.TestCase):

    def setUp(self):
        self.n = Naves()
        self.n1 = Nave('H', 8, 9, 3)
        self.n2 = Nave('L', 0, 1, 8)
        self.n3 = Nave('A', 9, 5, 2)
        agregar_nave(self.n, self.n1)
        agregar_nave(self.n, self.n2)
        agregar_nave(self.n, self.n3)
    
    def test_mostrar_nave(self):
        res = mostrar_nave(self.n1)
        self.assertEqual(res, 'La nave H con 8 metro(s) de largo. La tripulación es de 9 persona(s) y caben 3 pasajero(s)')
        self.assertNotEqual(res, 'La nave L con 0 metro(s) de largo. La tripulación es de 1 persona(s) y caben 8 pasajero(s)')
        
    def test_nombre(self): # Confirmamos que los nombres están ordenados de manera ascendente
        res = self.n.nombre.info
        self.assertEqual(res, 'A')
        self.assertNotEqual(res, 'H')
        self.assertNotEqual(res, 'J')
    
    def test_largo(self): # Confirmamos que el largo está ordenado de manera descendente
        res = self.n.largo.info
        self.assertEqual(res, 9)
        self.assertNotEqual(res, 8)
        self.assertNotEqual(res, 8)

    def test_tripulacion(self): # Confirmamos que la tripulación está ordenada de manera descendente
        res = self.n.tripulacion.info
        self.assertEqual(res, 9)
        self.assertNotEqual(res, 1)
        self.assertNotEqual(res, 5)

    def test_pasajeros(self): # Confirmamos que los pasajeros están ordenados de manera descendente
        res = self.n.pasajeros.info
        self.assertEqual(res, 8)
        self.assertNotEqual(res, 3)
        self.assertNotEqual(res, 2)

if __name__ == '__main__':
    unittest.main()