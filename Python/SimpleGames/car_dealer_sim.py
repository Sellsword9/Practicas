"""
Un juego basado en texto hecho en python,
donde el objetivo es, a resumidas cuentas,
comprar coches barato y venderlos caros.
"""
from cds_car_list import cars_prices, car_names_list

def main():
    """
    Modulo principal que controla el juego
    """
    turno = 1
    def avanzar_turno():
        turno += 1
    def tienda():
        print_coches(mny)
    def mercado():
        #TODO
        print("No programado")
    def restart():
        #TODO
        print("No programado")
    def opt():
        return input(
    """Escribe:
    1 para pasar al siguiente turno sin hacer nada
    2 para ver la lista de coches usados disponibles,
    3 para ver la lista de precios actuales de los coches
    4 para reiniciar """)
    opt_now = None
    def opt_again():
        main.opt_now = opt()

    mny = start()
    print(f"Tienes {mny} euros. Turno {turno}")
    dic_opts = {
        "1": avanzar_turno(),
        "2": tienda(), 
        "3": mercado(), 
        "4": restart()       
    }

    dic_opts.get(opt_now, opt_again())


def start():
    """
    Devuelve la cantidad de dinero inicial
    """
    return 1e6

main()

def print_coches(budget : int):
    """
    Muestra por pantalla
    una lista randomizada
    de 9 coches usados para comprar.
    Muestra de forma distinta los coches,
    en función de si pueden ser comprados o no
    """


