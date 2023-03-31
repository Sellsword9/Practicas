#![allow(unsed)]
use std::io; 
use rand::Rng; //Para generar numeros aleatorios
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;

fn main() {
    const NUMERO: i32 = 1_232_200;      //Constantes
    const PI: f64 = 3.141596;
    println!("Dime tu nombre");

    let mut nombre: String = String::new();
    io::stdin().read_line(&mut nombre) //Devuelve un enum que puede ser OK o Error
        .expect("No ha podido leer el nombre")

    println!("Hola, {}", nombre.trim_end());
}
