# Teoria de clase
# Archivos y carpetas en PowerShell
clear
New-Item -Path "C:\prueba" -ItemType Directory # Para crear un directorio
New-Item -Path "C:\prueba\fichero.txt" -ItemType File # Para crear un fichero
Get-ChildItem "C:\"
Read-Host "Pulsa intro para continuar"
#Añadir contenido a un fichero
# New-Item -Path "C:\prueba" -ItemType Directory 
# New-Item -Path "C:\prueba\fichero.txt" -ItemType File
Set-Content -Path "C:\prueba\fichero.txt" -Value "hola mundo" #Establece
Add-Content -Path "C:\prueba\fichero.txt" -Value "hola mundo 2" #Añade
Add-Content -Path "C:\prueba\fichero.txt" -Value "hola mundo 3"
Clear-Content -Path "C:\prueba\fichero.txt" #Deja el fichero vacio
New-item -Path "C:\prueba2"
Move-Item -Path "C:\prueba\fichero.txt" -Destination "C:\prueba2\fichero2.txt"  # Mover
Remove-Item -Path "C:\prueba\fichero.txt"
Remove-Item -Path "C:\prueba" 

