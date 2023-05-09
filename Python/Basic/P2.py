# pylint: disable=all
"""
Comprueba si un numero dado es primo o no
"""
def lista_divisores(x) -> list:
    """
    Devuelve una lista con todos los divisores de x
    """
    a = []
    if x >= 1:
        a = [b for b in range(2, x) if x%b==0]
    return a

filtro_primo = lambda n: not lista_divisores(n)

num = input("Introduce un numero positivo: ")

try:
    numero = abs(int(num))
    if filtro_primo(numero):
        print("Tu numero es primo")
    else:
        print("Tu numero no es primo")
        print("Sus divisores no triviales son: ")
        for a in lista_divisores(numero):
            print(a)
except ValueError:
    print("Error: Ingresa un valor numérico válido.")

input()