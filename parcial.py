tablero = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,1,0],
    [0,0,1,0,1],
    [0,0,0,0,1]
]
def batalla_naval():
    """
    Funcion con juego de batalla naval
    """
    def verificar_coordenadas(tablero:list,fila:int,columna:int)->bool:
        """
        La funcion verifica que en el en la columna, de la fila del tablero, haya un uno o un 0
        en caso de 0 retorna agua y en caso de 1 retorna hundido
        """
        if tablero[fila][columna] == 1:
            return "Hundido"
        else:
            return "Agua"
    seguir = "si"
    while seguir == "si":
        # Bucle
        fila = int(input("Ingrese el numero de fila en la que quiere tirar: "))
        while fila < 0 or fila > 4:
            fila = int(input("Error. Ingrese el numero de fila en la que quiere tirar: "))
        columna = int(input("Ingrese el numero de columna en la que quiere tirar: "))
        while columna < 0 or columna > 4:
            columna = int(input("Error. Ingrese el numero de columna en la que quiere tirar: "))
        print(verificar_coordenadas(tablero,fila,columna))
        seguir = input("Desea realizar otro tiro? si/no: ").lower()

batalla_naval()