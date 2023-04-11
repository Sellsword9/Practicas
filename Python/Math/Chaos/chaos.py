# Parámetros
R = 3.789 #Entre 3 y 4
X0 = 0.5 #Entre 0...1 y 0.999...

def formula(x: float):
    return R * x * (1 - x)

def generate_chaos(n):
    numbers = []
    x = X0
    for _ in range(n):
        x = formula(x)
        numbers.append(x)
    return numbers

# Generar los números per se
numbers = generate_chaos(100)

# Printear 
print("Generated pseudo-random numbers: ")
print(numbers)