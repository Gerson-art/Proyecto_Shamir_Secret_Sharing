from shamir_generate import random_prime_in_range
from shamir_generate import generar_puntos
from shamir_generate import reconstruir_secreto
import random
import numpy as np
partes = []
polynomial = []
prime=0
threshold=0

def main():
    
    print("1. Dividir secreto")
    print("2. Reconstruir secreto")
    print("3. Salir")
    option = input("Seleccione una opción: ")
    if option == "1":
        secret = int(input("Ingrese el secreto: "))
        umbral = int(input("Ingrese el threshold: "))
        n_points = int(input("Ingrese el número de shares: "))
        prime_num = random_prime_in_range(secret + umbral, 100)
        shares, polynom = generar_puntos(secret, n_points, umbral, prime_num)

        polynom= np.polynomial.Polynomial(polynom)

        global prime
        prime=prime_num
        global partes
        partes=shares
        global polynomial
        polynomial=polynom
        global threshold
        threshold=umbral

        print("Primo aleatorio utilizado:", prime_num)
        print("El secreto ha  sido divido en", n_points, "partes")
        print("Shares generados:", shares)
        print("El polinomio utilizado fue:", polynom)
        print("Ahora puede proceder a reconstruir el secreto")
        main()
        
    elif option == "2":
        
        if partes:
            shares_aleatorios= shares_random()
            print("Se seleccionaron "+str(threshold)+" shares de forma aleatoria para reconstruir el secreto")
            print("Shares aleatorios seleccionados:", shares_aleatorios)
            

            secret = reconstruir_secreto(shares_aleatorios, prime)
            print("Secreto reconstruido:", secret)

            print("¿Desea volver al menu?")
            print("1. Sí")
            print("2. No")
            option = input("Seleccione una opción: ")   
            if option == "1":
                reset_params()
                main()
            else:
                print("Gracias por utilizar el programa")
                return
            
        else:
            print("Primero debe dividir el secreto")
        main()

    else:
        print("Gracias por utilizar el programa")
        return    


def shares_random():
    global partes
    global threshold
    return random.sample(partes,threshold)


def reset_params():
    global partes
    global polynomial
    global prime
    global threshold
    partes = []
    polynomial = []
    prime = 0
    threshold = 0



if __name__ == "__main__":
    main()