from random import randint


class Cuenta_Corriente:
    def __init__(self, numero: int, saldo: float):
        if numero < 0 > saldo:
            raise ValueError("Valores negativos no soportados")
        self.numero = numero
        self.saldo = saldo
    def add_dinero(self, dinero: float):
        self.saldo += dinero
    def retirar_dinero(self, dinero: float):
        if (self.saldo < dinero):
            raise ValueError("No hay saldo suficiente en la cuenta")
        if (dinero < 0):
            raise ValueError("No se puede retirar un numero negativo")
        self.saldo -= dinero
    def hacer_transferencia(Cuenta1, Cuenta2, cantidad: float):
        can = Cuenta1.saldo >= cantidad
        if can:  
            Cuenta1.retirar_dinero(cantidad)
            Cuenta2.add_dinero(cantidad)
        return can
    def nueva_cuenta():
        c = Cuenta_Corriente(randint(1000, 9999),0)
        return c
        
""" def main():
    c = Cuenta_Corriente(1234, 100)
    c.add_dinero(20)
    c.retirar_dinero(100)
    print(c.saldo)
    c2 = Cuenta_Corriente(1234, 1)
    Cuenta_Corriente.hacer_transferencia(c, c2, 5)
    print(c2.saldo)
    c3 = Cuenta_Corriente.nueva_cuenta()
    print(c3.numero)
main() """