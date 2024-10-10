import sympy as sp
from fractions import Fraction

def reconstruct_polynomial(shares, p):
    x = sp.symbols('x')
    k = len(shares)
    polynomial = 0

    for j in range(k):
        xj, yj = shares[j]
        term = yj
        for m in range(k):
            if m != j:
                xm = shares[m][0]
                term *= (x - xm) / (xj - xm)
        polynomial += term

    # Simplificar el polinomio y tomar módulo p
    polynomial = sp.expand(polynomial)
    polynomial = polynomial.as_poly(x).all_coeffs()
    polynomial = [coeff % p for coeff in polynomial]

    polynomial = polynomial[::-1]

    return polynomial

def correct_polinom(shares,prime):
    polinom= reconstruct_polynomial(shares,prime)
    coefs=[]
    for num in polinom:
        fraccion = Fraction(num).limit_denominator()
        inv= pow(fraccion.denominator,-1,prime)
        coef= (fraccion.numerator*inv)%prime
        coefs.append(coef)
    return coefs




