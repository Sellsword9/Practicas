#!/bin/bash
# Autor: Yeray Romero
# Fecha: 2023/06/16
dir=$1

function comprobarDirectorio(){
if [[ ! -d $dir ]]; then
read -r -p "El directorio no existe. Enter para salir"
exit 127
fi
}

comprobarDirectorio

arr=()

function añadirFicheros() {
for fich in $(find $dir -type f );
do
arr+=($fich)
done
}

function menu {
read -r -p "Quieres mostrar todos los ficheros del directorio? S/n" resp
if [[ $resp == "S" || $resp == "s" ]]; then
    for fic in ${arr[@]}; do
    echo "$fic"
    sleep 1
    done
fi
}

añadirFicheros
menu
