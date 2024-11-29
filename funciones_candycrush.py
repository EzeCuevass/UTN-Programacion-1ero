import random
from Package_Input import Input
def generar_numeros(cantidad:int, fila:int, lista:list)-> None :
    """
    Genera numeros en la fila solicitada
    """
    i = 0
    while i < cantidad:
        lista[fila]["piezas"].append(random.randint(1,3))
        i+=1
def mostrar_lista(lista:list):
    for i in range(len(lista)):
        generar_numeros(7,i, lista)
        print(lista[i]["piezas"])

def verificar_eje(lista, fila, columna, numero, eje) -> int:
    """
    Funcion para contar los elementos iguales seguidos en cada eje
    """
    contador_iguales_eje = 0
    array_eje = []
    match eje:
        case "x":
            # Array de la fila seleccionada
            array_eje = lista[fila]["piezas"]
            # Divido el array con las posiciones que quedan hacia adelante, y las que quedan hacia atras
            posiciones_restantes_eje = array_eje[columna:]
            posiciones_anteriores_eje = array_eje[:columna]
            # Lo invierto para analizarlo con una funcion generica
            posiciones_anteriores_eje = posiciones_anteriores_eje[::-1]
        case "y":
            # Bucle que agarra todos los valores de la columna seleccionada, y los pone en un array
            for i in range(len(lista)):
                array_eje.append(lista[i]["piezas"][columna])
            # Divido el array con las posiciones que quedan hacia arriba, y las que quedan hacia abajo
            posiciones_restantes_eje = array_eje[fila:]
            posiciones_anteriores_eje = array_eje[:fila]
            # Lo invierto para analizarlo con una funcion generica
            posiciones_anteriores_eje = posiciones_anteriores_eje[::-1]
    # En el caso de no haber nada hacia adelante, no lo verifica (seria un array vacio)
    if posiciones_restantes_eje != None:
        contador_iguales_eje += verificar(posiciones_restantes_eje,numero)
    # En el caso de no haber nada hacia atras, no lo verifica (seria un array vacio)
    if posiciones_anteriores_eje != None:
        contador_iguales_eje += verificar(posiciones_anteriores_eje, numero)
    # Devuelvo los numeros iguales seguidos encontrados en el eje
    return contador_iguales_eje

def verificar_eleccion(lista:list, fila:int,columna:int):
    """
    Funcion para determinar si se ganaron 10 puntos, o si se sigue participando
    """
    # Guardo en una variable el numero seleccionado
    numero = lista[fila]["piezas"][columna]
    # Utilizo contadores con una funcion que devuelve los valores seguidos encontrados en cada eje
    contador_iguales_x = verificar_eje(lista, fila, columna, numero, "x")
    contador_iguales_y = verificar_eje(lista, fila, columna, numero, "y")
    print("X:   ",contador_iguales_x)
    print("Y:   ",contador_iguales_y)
    # En el caso de ser mayor a 2 alguno de los contadores, imprime 10 puntos, caso contrario imprime la frase 'segui
    # participando'
    if contador_iguales_x > 2 or contador_iguales_y > 2:
        print("HA GANADO 10 PUNTOS")
        return 10
    else:
        print("Segui participando!")
        return 0

def verificar(lista_posiciones:list ,numero:int) -> int:
    """
    Funcion para ver cuantos valores seguidos hay en un array
    """
    # Inicializo el contador en 0
    contador_iguales_eje = 0
    # Recorro el array y lo analizo
    for i in range(len(lista_posiciones)):
        # Si la posicion en la que esta iterando, es igual al numero pasado por parametro, suma uno al contador
        if lista_posiciones[i] == numero:
            contador_iguales_eje += 1
        # Caso contrario, rompe el loop, porque no es seguido
        else:
            break
    # Devuelvo la cantidad de iguales seguidos en el array
    return contador_iguales_eje

def nuevo_juego(lista:list):
    with open("scoreboard.csv", "r") as archivo:
        scoreboard = archivo.readlines()
        print("scoreboard actual: ")
        for persona in scoreboard:
            print(persona)
    nombre = Input.get_string("Ingresa tu nombre: ")
    puntos = verificar_eleccion(lista, 
                                Input.get_int("Ingrese el numero de fila: ", min=0, max=3),
                                Input.get_int("Ingrese el numero de columna: ", min=0, max=6))
    with open("scoreboard.csv", "a") as archivo:
        archivo.write(f"{nombre}, {puntos}\n")