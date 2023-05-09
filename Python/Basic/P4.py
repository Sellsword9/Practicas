# pylint: disable=all
"""
Lista todos los números primos en un rango dado y
muestra su suma
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

min = 2
max = -1

num = input("Introduce el valor mínimo como un numero positivo: ")

try:
    numero = abs(int(num))
    if numero < min:
        print("Numero demasiado pequeño, vuelve a intentarlo")
except ValueError:
    print("Error: Ingresa un valor numérico válido.")
    
min = numero

num = input("Introduce el valor máximo como un numero positivo: ")

try:
    numero = abs(int(num))
    if numero < min:
        print("Numero demasiado pequeño, vuelve a intentarlo")
except ValueError:
    print("Error: Ingresa un valor numérico válido.")
    
max = numero
primos = []
print(f"Los primos entre {min} y {max} son:")
for n in range(min, max+1):
    if filtro_primo(n):
        print(n)
        primos.append(n)
    
print(f"Su suma es: {sum(primos)}")
input()