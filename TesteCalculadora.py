import unittest
from calculadora import Calculadora
class Testcalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calculadora.adicao(2,3), 5)
        self.assertEqual(self.calculadora.adicao(-3,-6), -9)
        self.assertEqual(self.calculadora.adicao(0,0), 0)
    def test_subtrair(self):
        self.assertEqual(self.calculadora.subtracao(5,3), 2)
        self.assertEqual(self.calculadora.subtracao(-2,2), -4)
        self.assertEqual(self.calculadora.subtracao(-3,-3), 0)
    def test_multiplicar(self):
        self.assertEqual(self.calculadora.multiplicacao(3,4), 12)
        self.assertEqual(self.calculadora.multiplicacao(-2,-3), 6)
        self.assertEqual(self.calculadora.multiplicacao(-2,3), -6)
    def test_dividir(self):
        self.assertEqual(self.calculadora.divisao(10,2), 5)
        with self.assertRaises(ValueError):
            self.calculadora.divisao(10,0)

if __name__=="__main__":
    unittest.main()            