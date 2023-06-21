# Se relacionan ciudades y sus prefijos

prefijos = {
    'Granada': 23 ,
    'Madrid' : 91 ,
    'Jaen'   : 953
}

for a in prefijos:
    b = prefijos.get(a)
    print(f"Clave: {a}")
    print(f"Valor: {b}")