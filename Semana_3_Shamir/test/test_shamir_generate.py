import unittest
from shamir_generate import polinomio_aleatorio, evaluar_polinomio, generar_puntos, reconstruir_secreto, random_prime_in_range

class TestShamirGenerate(unittest.TestCase):

    def test_polinomio_aleatorio(self):
        secret = 5
        threshold = 3
        prime = 17
        coeficientes = polinomio_aleatorio(threshold, secret, prime)
        
        self.assertEqual(len(coeficientes), threshold)  # Verifica que el número de coeficientes sea igual al umbral
        self.assertEqual(coeficientes[0], secret)  # El primer coeficiente debe ser el secreto

    def test_evaluar_polinomio(self):
        coeficientes = [5, 3, 1]  # Polinomio: 5 + 3x + x^2
        x = 2
        resultado = evaluar_polinomio(coeficientes, x)
        self.assertEqual(resultado, 5 + 3*2 + 1*2**2)  # Evaluar el valor manualmente para comparar

    def test_generar_puntos(self):
        secret = 6
        n_puntos = 5
        threshold = 3
        prime = 23
        puntos, polinomio = generar_puntos(secret, n_puntos, threshold, prime)
        
        self.assertEqual(len(puntos), n_puntos)  # Verifica que el número de puntos generados sea correcto
        self.assertEqual(polinomio[0], secret)  # El primer coeficiente del polinomio debe ser el secreto

    def test_reconstruir_secreto(self):
        prime = 23
        shares = [(1, 5), (2, 10), (3, 3)]
        secret = reconstruir_secreto(shares, prime)
        
        self.assertIsInstance(secret, int)  # Verifica que el secreto reconstruido sea un entero

    def test_random_prime_in_range(self):
        start = 10
        end = 50
        prime = random_prime_in_range(start, end)
        
        self.assertTrue(start <= prime <= end)  # Verifica que el primo esté en el rango dado
        self.assertTrue(all(prime % i != 0 for i in range(2, prime)))  # Verifica que el número sea primo

if __name__ == '__main__':
    unittest.main()
