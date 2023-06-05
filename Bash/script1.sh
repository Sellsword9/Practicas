#!/bin/bash
# Author: Yeray Romero
# Date: 2023/06/05
# Create a example menu
fn_files(){
    # List all files in given directory
    read -r -p "Enter directory: " directory
    ls -l "$directory"
}
fn_joke(){
    # Tell a joke
    echo "yyyy/mm/dd is not the best date format to use"
}
fn_pi(){
    # Give first 1000 numbers of PI
    echo "scale=1000; 4*a(1)" -n | bc -l
}
main_menu(){
    echo "1. List files in a directory"
    echo "2. Tell me a joke"
    echo "3. Give me first 1000 numbers of PI"
    echo "4. Exit"
    read -r -p 'Please enter option [1 - 4]: ' option
    if [ "$option" = "1" ]; then
        fn_files
    elif [ "$option" = "2" ]; then
        fn_joke
    elif [ "$option" = "3" ]; then
        fn_pi
    elif [ "$option" = "4" ]; then
        exit
    else
        echo "Please enter a valid option"
        read -p "Press [enter] key to continue..." -r
    fi
}
main_menu