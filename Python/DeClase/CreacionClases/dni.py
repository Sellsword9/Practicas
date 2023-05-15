
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
        self.letra = self.__calcular_letra(self.numero)
    
    def __calcular_letra(self, n: int) -> str:
        """ Este metodo calcula la letra en base al numero"""
        lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
                 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
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
    def __bool__(self) -> bool:
        """Convierte el objeto en boolean"""
        return bool(self.numero)
    def __int__(self) -> int:
        """
        Este método convierte el dni en un numero entero,
        suponiendo que eso se hace devolviendo su numero
        """
        return int(self.numero)
    def __str__(self) -> str:
        """Convierte el dni en su representacion str"""
        return f"{self.numero}{self.letra}"

def crearDni(s: str) -> dni:
    """
    Crea un dni a partir de un string
    """
    return dni(int(s))

        