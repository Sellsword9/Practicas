# pylint: disable=all
# Lista todos los números primos entre un rango dado 

"""
Crea un programa que genere una lista de los primeros N números primos.
El usuario debe poder especificar el valor de N como entrada."
"""
def lista_divisores(x):
    a = []
    if not x <= 1:
        a = [a for a in range(2, x) if x%a==0]
    return a

filtro_primo = lambda n: not lista_divisores(n)
try:
    num = input("Introduce cúantos numeros primos quieres, como un numero positivo(Min: 1): ")
    min = input("Introduce el numero desde el que quieres empezar, como un numero positivo(Min: 2):  ")
    numero = abs(int(num))
    minimo = abs(int(min))
    if numero <= 0 or minimo <= 1:
        print("Numero demasiado pequeño, vuelve a intentarlo")
    # calcular "numero" primos desde minimo
    primos = []
    n = minimo
    while len(primos) < numero:
        if filtro_primo(n):
            primos.append(n)
        n += 1
    print(f"Los {numero} primeros primos desde {minimo} son:")
    for primo in primos:
        print(primo)
except ValueError:
    print("Error: Ingresa un valor numérico válido.")


