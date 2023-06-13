#!/bin/bash
# @author: Yeray Romero
# @date: 13/06/2023
# @description: Script para comprimir a tar.gz
function numParametros(){
    if [ $# -ne 2 ]; then
        echo "Error, numero de parametros incorrecto"
        exit 1
    fi
}