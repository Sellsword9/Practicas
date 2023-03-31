use std::io;

fn primo(n: u32) -> bool {
    let mut primo: bool = true;
    if n <= 1 {
        primo = false;
    }
    let raiz: (n as f64).sqrt() as u32; //Calcula la raíz cuadrada del número. (*1)
    for i in 2..=raiz { //El bucle busca desde 2 (minimo numero primo) hasta la raiz
        if n % i == 0 {
            primo = false;
        }
    }
    return primo;
}

fn main() {
    println!("Introduce un numero primo:");
    let mut input = String::new(); 
    io::stdin().read_line(&mut input).expect("Failed to read input.");
    let num = input.trim().parse::<u32>().expect("Por favor introduce un entero positivo");

    if is_prime(num) {
        println!("Tu ganas. {} es, de hecho, un primo", num);
    } else {
        println!("No. {} no es primo", num);
    }
}
//(*1) 
//Calcular la raíz cuadrada tiene su motivo.
//si x*x = n, 
//ningún divisor de n puede ser mayor que x
//salvo que exista ya uno menor que x

