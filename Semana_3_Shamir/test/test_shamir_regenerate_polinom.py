import unittest
from shamir_regenerate_polinom import reconstruct_polynomial, correct_polinom

class TestShamirRegeneratePolinom(unittest.TestCase):

    def test_reconstruct_polynomial(self):
        shares = [(1, 6), (2, 13), (3, 28)]
        prime = 31
        polinomio = reconstruct_polynomial(shares, prime)
        
        self.assertIsInstance(polinomio, list)  # Verifica que el resultado sea una lista
        self.assertGreaterEqual(len(polinomio), 2)  # Verifica que el polinomio tenga al menos un término no constante

    def test_correct_polinom(self):
        shares = [(1, 6), (2, 13), (3, 28)]
        prime = 31
        polinomio = correct_polinom(shares, prime)
        
        self.assertIsInstance(polinomio, list)  # Verifica que el resultado sea una lista
        self.assertTrue(all(isinstance(coef, int) for coef in polinomio))  # Verifica que todos los coeficientes sean enteros

if __name__ == '__main__':
    unittest.main()
