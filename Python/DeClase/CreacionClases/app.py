from dni import dni
from dni import crearDni

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