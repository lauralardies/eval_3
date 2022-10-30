import unittest
from star_wars import Naves, Nave, agregar_nave, mostrar_nave

class TestNaves(unittest.TestCase):

    def setUp(self):
        self.n = Naves()
        self.n1 = Nave('H', 8, 9, 3)
        self.n2 = Nave('L', 8, 1, 3)
        self.n3 = Nave('A', 9, 5, 2)
        agregar_nave(self.n, self.n1)
        agregar_nave(self.n, self.n2)
        agregar_nave(self.n, self.n3)

if __name__ == '__main__':
    unittest.main()