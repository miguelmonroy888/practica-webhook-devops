import unittest
from app import sumar, restar, multiplicar

class TestCalculadora(unittest.TestCase):

    def test_suma_correcta(self):
        """Prueba que 2 + 2 sea 4"""
        resultado = sumar(2, 2)
        self.assertEqual(resultado, 4)

    def test_resta_correcta(self):
        """Prueba que 5 - 3 sea 2"""
        resultado = restar(5, 3)
        self.assertEqual(resultado, 2)
        
    # Prueba nueva
    def test_multiplicacion(self):
        """Prueba que 3 * 3 sea 9"""
        self.assertEqual(multiplicar(3, 3), 9)

if __name__ == '__main__':
    unittest.main()