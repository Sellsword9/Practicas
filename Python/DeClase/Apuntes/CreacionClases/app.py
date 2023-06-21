from dni import *

d = dni(123123123)

print(d.letra)
print(d.ultimo_digito_par())

if d:
    print("El numero no es cero")
else:
    print("El numero ES cero")
    
cuenta = 2 + 11232 + int(d)
print(cuenta)


print(d)

print("--------------  Parte de la persona nadadora  --------------")

per = Persona("Paco", 12)
per.nadar()

print("--------------  Parte de la caja  --------------")

caja = Caja()
caja.abrir_caja()
if (caja):
    caja.cambiar_mensaje(input("Introduce tu mensaje: "))
    if (caja.get_mensaje() == "falla"):
        caja.abierto = False
print("Tu mensaje ha sido: ", caja.get_mensaje())
print("Prueba otra vez y introduce el mensaje 'falla' para que el programa cierre la caja y falle al intentar acceder")