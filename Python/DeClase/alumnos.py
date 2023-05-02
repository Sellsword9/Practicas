"""
Este programa tiene una lista rellenada con información de varios alumnos
Nos mostrará un menú con el que podremos añadir un nuevo alumno y ver los
datos de los alumnos que ya hay
"""

alumnos = [
    {"nombre" : "Ismael", "Nota" : 7.5, "Edad" : 20},
    {"nombre" : "Pablo", "Nota" : 5, "Edad" : 18, "Direccion" :
                                                                {
                                                                    "Ciudad" : "Granada",
                                                                    "Calle" : "C/Albondon",
                                                                    "numero" : 10
                                                                } 
    },
    {"nombre": "Yeray", "nota":7.15}
    
    
]

def add_alumno():
    nom = input("Introduce el nombre")
    edad_str = input("Introduce la edad")
    edad = int(edad_str)
    nota_str = input("Introduce la nota")
    nota = int(nota_str)
    alumnos.append({"nombre" : nom, "edad": edad, "nota": nota})