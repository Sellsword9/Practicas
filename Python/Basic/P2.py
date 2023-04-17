# Se pregunta un numero y se dice si es primo o no
def lista_divisores(x):
    a = []
    if not(x <= 1):
        a = [a for a in range(2, x) if x%a==0]
    return a

filtro_primo = lambda n: not bool(lista_divisores(n))

num = input("Introduce un numero: ")

try:
    numero = int(num)
    if filtro_primo(numero):
        print("Tu numero es primo")
    else:
        print("Tu numero no es primo")
        print("Sus divisores no triviales son: ")
        for a in lista_divisores(numero):
            print(a)
except ValueError:
    print("Error: Ingresa un valor numérico válido.")