from shamir_generate import random_prime_in_range
from shamir_generate import generar_puntos
from shamir_generate import reconstruir_secreto
from shamir_regenerate_polinom import correct_polinom
import random
import numpy as np


def main():
    
    print("1. Dividir secreto")
    print("2. Reconstruir secreto")
    print("3. Obtener polinomio a partir de shares")
    print("4. Salir")
    option = input("Seleccione una opción: ")
    if option == "1":
        print("\n")
        secret = int(input("Ingrese el secreto: "))
        umbral = int(input("Ingrese el umbral: "))
        n_points = int(input("Ingrese el número de shares: "))
        print("\n")
        prime_num = random_prime_in_range(secret + umbral, 100)
        shares, polynom = generar_puntos(secret, n_points, umbral, prime_num)

        polynom= np.polynomial.Polynomial(polynom)

        print("Umbral utilizado (utilizará este valor más adelante):", umbral)
        print("Primo aleatorio utilizado (recuerde este valor):", prime_num)
        print("El secreto ha  sido divido en", n_points, "partes")
        print("Shares generados (copiar para más adelante):", shares)
        print("El polinomio utilizado fue:", polynom)
        print("\n")
        print("Ahora puede proceder a reconstruir el secreto")
        print("\n")
        main()
        
    elif option == "2":
            print("\n")
            print("Siguiendo el formato (x1,y1), (x2,y2), ... ,(xn,yn)")
            print("Puede copiar y pegar los shares generados en la opción 1")
            print("\n")
            shares_str = input("Ingrese los n shares separados por coma: ")
            threshold = int(input("Ingrese el umbral utilizado: "))
            prime = int(input("Ingrese el primo utilizado: "))
            print("\n")
            shares_str = shares_str.replace("(", "").replace(")", "")
            elementos = shares_str.split(", ")
            shares = [(int(elementos[i]), int(elementos[i + 1])) for i in range(0, len(elementos), 2)]
            shares= random.sample(shares,threshold)
            print("Se seleccionaron "+str(threshold)+" shares de forma aleatoria para reconstruir el secreto")
            print("Shares aleatorios seleccionados:", shares)
            print("\n")
            secret = reconstruir_secreto(shares, prime)
            print("Secreto reconstruido:", secret)
            print("¿Desea volver al menu?")
            print("1. Sí")
            print("2. No")
            option = input("Seleccione una opción: ")   
            if option == "1":
                
                main()
            else:
                print("Gracias por utilizar el programa")
                return
            
       

    elif option == "3":
        shares= []
        print("\n")
        print("Siguiendo el formato (x1,y1), (x2,y2), ... ,(xn,yn)")
        print("Puede copiar y pegar los shares generados en la opción 1")
        print("\n")
        shares_str = input("Ingrese los shares separados por coma: ")  
        umbral= int(input("Ingrese el umbral utilizado: "))
        prime= int(input("Ingrese el primo utilizado: "))

        shares_str = shares_str.replace("(", "").replace(")", "")
        elementos = shares_str.split(", ")

        shares = [(int(elementos[i]), int(elementos[i + 1])) for i in range(0, len(elementos), 2)]
        shares= random.sample(shares,umbral)
        polinomio= correct_polinom(shares,prime)  
        polinomio= np.polynomial.Polynomial(polinomio)
        print("\n")
        print("Polinomio reconstruido:", polinomio)
        print("¿Desea volver al menu?")
        print("1. Sí")
        print("2. No")
        option = input("Seleccione una opción: ")
        if option == "1":
            main()
        else: 
            print("Gracias por utilizar el programa")
            return    

    else:
        print("Gracias por utilizar el programa")
        return    









if __name__ == "__main__":
    main()