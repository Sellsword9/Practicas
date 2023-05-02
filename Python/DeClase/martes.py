"""
Varias funciones basicas
"""
def calcular_maximo(a,b,c):
    """
    Devuelve el maximo, calculado a lo bruto
    """
    max = a
    if b>c and b>a:
        max=b
    elif c>b and c>a:
        max=c
    return c
    