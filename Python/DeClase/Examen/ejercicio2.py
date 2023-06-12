ingresos: tuple[int] = (
15000, 16000,
10000, 9000 ,
12000, 13000, 
7000 , 6000 , 
11000, 13000, 
14000, 15000)
gastos: tuple[int] = (
 8000 , 9000,
 11000, 10000,
 12000, 10000,
 9000 , 8000 ,
 9000 , 9000 ,
 12000, 14000
 )
meses: dict[str, int] = {
    "enero": 1, "febrero": 2,
    "marzo" : 3, "abril" : 4,
    "mayo": 5 , "junio": 6,
    "julio": 7, "agosto" : 8,
    "septiembre" : 9, "octubre" : 10,
    "noviembre": 11, "diciembre" :12
}

def calcular_media(fuente: tuple[int]):
    return sum(fuente) / 12.0

def main():
    print("Balances:")
    for mes in meses:
        count = meses.get(mes) - 1
        print(f"{mes}: \n Balance: {ingresos[count] - gastos[count]}")
    print("Media de ingresos anual: " + str(calcular_media(ingresos)))
    print("Media de gastos anual: " + str(calcular_media(gastos)))
    print(f"Balance final:{sum(ingresos) - sum(gastos)}")
main()