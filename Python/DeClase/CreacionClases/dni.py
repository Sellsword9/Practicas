
class dni:
    """
    Esta clase representa un dni con su letra
    """
    def __init__(self, n: int):
        """
        Este método es el constructor.
        Recibe:
        self --> El objeto que se crea
        n --> es el número del dni que vamos a ponerle
        """
        #Esto añade el numero al objeto
        self.numero = n
        #Esto añade la letra
        self.letra = self.calcular_letra(self.numero)
    
    def calcular_letra(self, n: int) -> str:
        """ Este metodo calcula la letra en base al numero"""
        lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
                 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'
                 ]
        return lista[ n % len(lista)]
    def get_ultimo_digito(self) -> str:
        """
        Devuelve el ultimo digito del numero
        """
        return str(self.numero)[-1]
    def ultimo_digito_par(self) -> bool:
        """
        Devuelve si el ultimo digito es par o no
        """
        return not self.numero % 2    