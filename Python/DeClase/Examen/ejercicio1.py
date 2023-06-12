"""
    Ejercicio 1 del examen de Python:
    Conversor de monedas
"""
def preguntar_cantidad() -> float:
    cantidad: float = 0.0
    try:
        cantidad = float(input("Introduce la cantidad a convertir:  \n "))
    except ValueError:
        print("Eso no es un numero valido, prueba otra vez")
        preguntar_cantidad()
    if (cantidad < 0):
        raise ValueError("Los numeros negativos no son validos")
    return cantidad 
conversor: dict[str, float] = {
    "dolar": 1.42,
    "libra": 0.87,
    "yen" : 113.86,
    "peseta": 166.38
}
def preguntar_moneda() -> str:
    moneda = input("Introduce la moneda a la que deseas convertir: \n")
    moneda = moneda.lower()
    if moneda not in conversor:
        raise ValueError(f"La moneda {moneda} no está admitida")
    else:
        return moneda
    
def convertir(moneda: str, cantidad: float) -> float:
    """
    Usa una moneda ya validada y una cantidad (euros)
    para convertirlo a la moneda enviada. Devuelve un float con la cantidad en la moneda
    Argumentos: 
    moneda: La moneda a la que convertir
    cantidad: la cantidad de euros que convertir a dicha moneda
    Devuelve:
    La cantidad en la moneda seleccionada
    """
    return conversor.get(moneda) * cantidad

def main():
    moneda = preguntar_moneda()
    cantidad = preguntar_cantidad()
    resultado = convertir(moneda, cantidad)
    print(f"{cantidad} euros equivalen a {resultado} {moneda}.")

main()