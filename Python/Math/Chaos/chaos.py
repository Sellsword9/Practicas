# Crea números aleatorios entre 0 y 1
# Parámetros
R = 3.789 #Entre 3 y 4
X0 = 0.5 #Entre 0...1 y 0.999...

def formula(x: float):
    return R * x * (1 - x)

def generate_chaos(n):
    g = []
    x = X0
    for _ in range(n):
        x = formula(x)
        g.append(x)
    return g

# Generar los números per se
numbers = generate_chaos(100)

# Printear 
print("Generated pseudo-random numbers: ")
for a in numbers:
    print(a)
