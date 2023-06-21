# Vamos a hacer un programa que pregunta tu nombre y te saluda
nombre = input("Dime tu nombre: ")
edad=input("Dime tu edad: ")

# Forma basica
# print("Te llamas", nombre, "y tu edad es", edad)
# Otra forma basica 
# print("Te llamas {} y tu edad es {}".format(nombre, edad))
# Forma de Java (solo string)
# print("Te llamas " + nombre + " y tu edad es " + edad)

print(f"Te llamas {nombre} y tu edad es {edad}")
