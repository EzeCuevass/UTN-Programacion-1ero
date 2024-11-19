import random

lista = [
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]}
]

def generar_numeros(cantidad:int, fila:int)-> None :
    """
    Genera numeros en la fila solicitada
    """
    i = 0
    while i < cantidad:
        lista[fila]["piezas"].append(random.randint(1,3))
        i+=1

for i in range(len(lista)):
    generar_numeros(7,i)
    print(lista[i]["piezas"])


def verificar(lista:list ,numero:int) -> int:
    contador_iguales_x = 0
    for i in range(len(lista)):
            if lista[i] == numero:
                print(f"{lista[i]} es igual a {numero}")
                contador_iguales_x += 1
            else:
                print(f"{lista[i]} NO es igual a {numero}")
                break
    return contador_iguales_x

def verificar_eleccion(fila:int,columna:int):
    numero = lista[fila]["piezas"][columna]
    array_x = lista[fila]["piezas"]
    contador_iguales_x = 0
    contador_iguales_y = 0
    posiciones_restantes_x = array_x[columna:]
    posiciones_anteriores_x = array_x[:columna]
    posiciones_anteriores_x = posiciones_anteriores_x[::-1]
    array_y = []
    for i in range(len(lista)):
        array_y.append(lista[i]["piezas"][columna])
    posiciones_restantes_y = array_y[fila:]
    posiciones_anteriores_y = array_y[:fila]
    posiciones_anteriores_y = posiciones_anteriores_y[::-1]
    if posiciones_restantes_x != None:
        contador_iguales_x += verificar(posiciones_restantes_x,numero)
    if posiciones_anteriores_x != None:
        contador_iguales_x += verificar(posiciones_anteriores_x, numero)
    if posiciones_restantes_y != None:
        contador_iguales_y += verificar(posiciones_restantes_y, numero)
    if posiciones_anteriores_y != None:
        contador_iguales_y += verificar(posiciones_anteriores_y, numero)
    if contador_iguales_x or contador_iguales_y > 2:
        print("HA GANADO 10 PUNTOS")
verificar_eleccion(int(input("Ingresa el numero de fila: ")), int(input("Ingresa el numero de columna: ")))