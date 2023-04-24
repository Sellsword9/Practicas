# pylint: disable=all
# Se pregunta un numero y se dice si es primo o no
"""
Encuentra todos los factores primos del numero introducido
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
        # Sacar todos los factores primos del numero
        factores = []
        for a in lista_divisores(numero):
            if filtro_primo(a):
                factores.append(a)
        print("Sus factores primos son: ")
        for a in factores:
            print(a)
except ValueError:
    print("Error: Ingresa un valor numérico válido.")