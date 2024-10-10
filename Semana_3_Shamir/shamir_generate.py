from random import randint
import sympy
import random
from shamir_regenerate_polinom import correct_polinom


def polinomio_aleatorio(threshold, secret,prime):

    coeficientes = [secret] + [randint(0, prime-1) for _ in range(threshold-1)]
    return coeficientes

def evaluar_polinomio(coeficientes, x):
    resultado = 0
    for i, coef in enumerate(coeficientes):
        resultado += coef * x**i
    return resultado

def generar_puntos(secret,n_puntos,threshold,prime):
    polinomio = polinomio_aleatorio(threshold, secret,prime)
    puntos = []
    for i in range(1,n_puntos+1):
        
        y = evaluar_polinomio(polinomio, i)%prime
        puntos.append((i, y))
    return puntos,polinomio

def reconstruir_secreto(shares,prime):
    
    def interpolacion_lagrange(x, x_s, y_s):
        def polinomio_lagrange(j):
            num = 1
            den = 1
            result=1
            for m in range(len(x_s)):
                if m != j:
                    num = (x - x_s[m])
                    den = pow((x_s[j] - x_s[m]),-1,prime)
                    result *= ( num * den)%prime
            return result

        result = 0
        for j in range(len(y_s)):
            result += ((y_s[j] * polinomio_lagrange(j)))%prime
        return result

    x_s, y_s = zip(*shares)
    return (interpolacion_lagrange(0, x_s, y_s))%prime

def random_prime_in_range(start, end):
    primes = list(sympy.primerange(start, end))
    if primes:
        return random.choice(primes)
    else:
        return None  



"""
secret= int(input("Ingrese el secreto: "))
threshold= int(input("Ingrese el threshold: "))
n_puntos= int(input("Ingrese el número de puntos: "))
prime=random_prime_in_range(secret+threshold, 100)

shares,polinomio = generar_puntos(secret,n_puntos,threshold,prime)
shares=random.sample(shares,threshold)
polinomio_reconstruido= correct_polinom(shares,prime)

print("Número primo utilizado: ",prime)
print("Lista de shares:",shares)
print("Polinomio original generado:",polinomio)
print("Polinomio reconstruido:",polinomio_reconstruido)
print("Secreto revelado:",reconstruir_secreto(shares,prime))

"""


