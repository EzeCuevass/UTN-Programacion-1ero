def mostrar_objetos_array(array:list) -> None:
    """
    Toma un array conformado por objetos, y muestra por cada clave, el valor.
    """
    for objeto in array:
        keys = (objeto.keys())
        for key in keys:
            print(f"{key} : {objeto[key]}")
        print("\n")

def filtrar_por_clave(array:list, clave:str, valor) -> list:
    """
    Funcion que se utiliza para filtrar un array, retorna el array que contienen los objetos que el valor coincide
    con el pasado por parametros
    """
    filtrado = []
    for objeto in array:
        if objeto[clave] == valor:
            filtrado.append(objeto)
    return filtrado
def ordenar_por_clave(array:list, clave:str, orden:int=1) -> None:
    """
    Ordena array de diccionarios, comparando el valor de la clave pasada por parametro, si no recibe parametro de
    orden, ordena ascendentemente, en el caso de recibirlo, si es 1 ordena ascendentemente, si es -1 de manera 
    descendente
    """
    if orden == 1:
        for i in range(len(array)):
            for j in range(i,len(array)):
                if array[i][clave] > array[j][clave]:
                    aux = array[j]
                    array[j] = array[i]
                    array[i] = aux
    elif orden == -1:
        for i in range(len(array)):
            for j in range(i,len(array)):
                if array[i][clave] < array[j][clave]:
                    aux = array[j]
                    array[j] = array[i]
                    array[i] = aux
    mostrar_objetos_array(array)

def establecer_min_max(bandera,minmax,posicion, i, clave, array):
    """
    Establece el minimo o el maximo, tomando como referencia los datos pasados por parametro.
    """
    bandera = False
    min_max = int(array[i][clave])
    posicion = i
def obtener_min_max_por_clave(array:list, clave:str, opcion:int) -> int:
    """
    Obtiene el minimo o el maximo de la lista de objetos, y retorna su posicion
    """
    min_max = 0
    bandera = True
    posicion = 0
    if opcion == 1:
        for i in range(len(array)):
            if array[i][clave] > min_max or bandera:
                establecer_min_max(bandera, min_max, posicion, i, clave, array)
        return posicion
    elif opcion == -1:
        for i in range(len(array)):
            if array[i][clave] < min_max or bandera:
                establecer_min_max(bandera, min_max, posicion, i, clave, array)
        return posicion

def contador_valor(array:list, clave:str, valor) -> int:
    """
    Cuenta cuantas veces esta el valor en un array de objetos
    """
    contador = 0
    for objeto in array:
        if objeto[clave] == valor:
            contador += 1
    return contador

def obtener_set_valores(array:list, clave:str):
    """
    Crea un set de valores encontrados en un array.
    """
    set_nuevo = set()
    for objeto in array:
        set_nuevo.add(objeto[clave])
    return set_nuevo

def promedio_por_clave(array:list,clave:str):
    """
    Funcion que obtiene el promedio de un array, basandose en el valor de la clave pasada por parametro.
    """
    total = 0
    for objeto in array:
        total += int(objeto[clave])
    promedio = total / len(array)
    return promedio


def agregar_clave(objeto:dict, clave, valor):
    """
    Funcion para agregar clave a un diccionario.
    Params: Clave ; Valor
    """
    objeto[clave] = valor
