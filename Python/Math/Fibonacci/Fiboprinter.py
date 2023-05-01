def fibo(num_par: int):
    nums = []
    if num_par < 2:
        nums.append(2)
    else:
        print("something")
try:
    num = input("Introduce cúantos numeros quieres, como un numero positivo(Min: 1): ")
    numero = abs(int(num))
    numeros = []
    while len(numeros) < numero:
        print("something")
    print(f"Los {numero} primeros numeros de la sucesión son: ")
    for numDeFibo in numeros:
        print(numDeFibo)
except ValueError:
    print("Error: Ingresa un valor numérico válido.")