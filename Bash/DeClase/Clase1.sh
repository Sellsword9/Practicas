#!/bin/bash
# Author: Yeray Romero
# Comando para crear usuarios
# useradd -m -d /home/usuario -s /bin/bash nombre_usuario
# Comando para cambiar el dueño de un fichero
# chown nombre_usuario:nombre_grupo fichero
# Cambiar el dueño de todos los ficheros que no comiencen por a
sudo chown root /test/[^a]*
# r w x 

##
cp -R /etc/[aeiou]* /ruta

## stat
stat -c %n--%s TareaTema4.sql

## 
groupadd

## 
mv /ruta/*[]* /ruta2 # Mueve el fichero a la ruta2

# Para comprimir
tar -czvf copia.tar.gz /test/h.text
# Para mover
mv copia.tar.gz /test2
##
find /home/ -type f -name "*html" -size -500l -ctime -2 -exec ls -la {} \;
##
ip a | grep "inet " | grep "global" | tr -s " " "|" | cut -d "|" -f 3
## 
grep "^-"
##
grep -v "^-"
##
cut -d "|" -f5,9 | sort -nr -t "|" -k2 | head -1
##
ls -Rla
##

