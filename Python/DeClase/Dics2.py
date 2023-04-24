"""
Probando los diccionarios con multivalores y anidados
"""
clase = {
    "dni1":{"nombre":"Paco", "edad":19},
    "dni2":{"nombre":"Pepe", "edad":18},
    "dni3":{"nombre":"Jorge", "edad":15}
}
# print(clase)
print(clase["dni1"]['nombre'])

for a in clase:
    """
    Para todas las claves, printea "nombre: edad"
    """
    b = clase[a]
    print(b['nombre'], ": ", b['edad'], sep="")
