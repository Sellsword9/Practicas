# cds_car_list.py
"""
Almacena los precios 
y los nombres de los coches
"""
cars_prices = {
    "Laguar Basic" : 2e4,
    "Laguar Festa" : 2.3e4,
    "Lazero Mantra": 6e4,
    "Lazero Dante ": 9.5e4,
    "Parry Pat": 1.2e5,
    "Mento Patan": 4e5 
}
def car_prices_list():
    """
    Devuelve un diccionario
    con los nombres/precios 
    de los coches
    """
    return cars_prices
def car_names_list():
    """
    Devuelve una lista
    de str de los nombres
    de los coches,
    sin el precio
    """
    lista_coches = []
    for car in car_prices_list():
        lista_coches.append(car)
    return lista_coches
