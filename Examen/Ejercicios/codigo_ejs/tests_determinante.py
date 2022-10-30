import unittest
from sarrus import submatriz, determinante

class TestDeterminante(unittest.TestCase):

    def setUp(self):
        self.matriz = [[1, 0, 2],
            [3, 0, 0],
            [2, 1, 4]]

    def test_submatriz(self):
        res = submatriz(self.matriz, 0, 0)
        self.assertEqual(res, [[0, 0], [1, 4]])
        self.assertNotEqual(res, [[3, 0], [2, 4]])
    
    def test_determinante(self):
        res = determinante(self.matriz)
        self.assertEqual(res, 6)
        self.assertNotEqual(res, 9)

if __name__ == '__main__':
    unittest.main()