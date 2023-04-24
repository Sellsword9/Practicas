"""
Crea números aleatorios entre 0 y 1
"""
# Parámetros
R = 3.789 #Entre 3 y 4
X0 = 0.5 #Entre 0...1 y 0.999...

def formula(x: float):
    """
    Devuelve el resultado de la aplicación de la fórmula
    """
    return R * x * (1 - x)

def generate_chaos(repeticiones: int):
    """
    Genera los números aleatorios
    """
    num_list = []
    x = X0
    for _ in range(repeticiones):
        x = formula(x)
        num_list.append(x)
    return num_list

# Generar los números per se
numbers = generate_chaos(100)

# Printear
print("Numeros generados: ")
for a in numbers:
    print(a)
