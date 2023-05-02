'''
Una libreria con varias funciones
'''
def calcular_area_rectangulo(base: int, altura: int) -> int:
    """
    Devuelve el area de un rectangulo
    """
    if base<0 or altura<0:
        raise ValueError("Un numero es negativo")
    return base * altura
def es_positivo(numero: int) -> bool:
    """Devuelve true si es positivo"""
    return numero > 0
def calcular_area_cuadrado(lado: int) -> int:
    return calcular_area_rectangulo(lado, lado)
def funcion_compleja(numero):
    """
    Devuelve false si el numero es cero,
    si es 1, devuelve "uno",
    si es 2, devuelve un diccionario,
    si es 3, devuelve 4.27
    en cualquier otro caso, lanza ValueError
    """
    #TODO