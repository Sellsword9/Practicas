# pylint: disable=all
# Lista todos los números primos entre un rango dado

def lista_divisores(x):
    a = []
    if not x <= 1:
        a = [a for a in range(2, x) if x%a==0]
    return a

filtro_primo = lambda n: not bool(lista_divisores(n))

def preguntar_numero():
    num = input("Introduce el valor mínimo como un numero positivo: ")

    try:
        numero = abs(int(num))
        if numero < min:
            print("Numero demasiado pequeño, vuelve a intentarlo")
            preguntar_numero()
    except ValueError:
        print("Error: Ingresa un valor numérico válido.")
        preguntar_numero()
    return numero


min = preguntar_numero()
max = preguntar_numero()

print("Los primos entre esos dos valores son:")
for n in range(min, max):
    if filtro_primo(n):
        print(n)
