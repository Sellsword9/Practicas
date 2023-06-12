from ejercicio4 import Cuenta_Corriente
clientes: dict[str, tuple[Cuenta_Corriente]] = {
    "Pedro Lopez" : (Cuenta_Corriente(1234, 5000),
                     Cuenta_Corriente(5678, 1200)),
    "Luisa Perez" : (Cuenta_Corriente(4492, 800),
                     Cuenta_Corriente(2112, 9000)),
    "Antonio Gonzalez" : (Cuenta_Corriente(1251, 6000)),
    "John Perez" : (Cuenta_Corriente(7212, 5200),
                    Cuenta_Corriente(4442, 8900),
                    Cuenta_Corriente(9878, 6000))
}
def calcular_saldo_cliente(cliente: str) -> float:
    cuentas = clientes.get(cliente)
    suma = 0
    if not type(cuentas) == Cuenta_Corriente:
        for cuenta in cuentas:
            suma += cuenta.saldo
    else:
        suma = cuentas.saldo
    return suma

def calcular_cuentas_cliente(cliente: str) -> int:
    total = 0
    cuentas = clientes.get(cliente)
    if not type(cuentas) == Cuenta_Corriente:
        total = len(cuentas)
    else:
        total = 1
    return total

def main():
    cliente = input("Introduce el nombre de un cliente: ")
    if  cliente not in clientes:
        print("El cliente no está en el banco")
    else:
        print("Si que está en el banco.")
        saldo = calcular_saldo_cliente(cliente)
        cuentas = calcular_cuentas_cliente(cliente)
        print(f"La suma de sus saldos es: {saldo} ")
        print(f"Este cliente tiene en total {cuentas} cuentas")

main()