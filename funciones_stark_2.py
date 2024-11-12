import json
def leer_json(nombrearchivo:str, lista:str) -> list:
    try:
        with open(nombrearchivo, "r") as j:
            archivo = json.load(j)
            return archivo[lista]
    except ValueError:
        print("error")

def generar_csv(nombrearchivo:str, lista: str):
    if lista != []:
        array_contenido = []
        for objeto in lista:
            linea = objeto_a_csv(objeto) + "\n"
            array_contenido.append(linea)
            # guardar_archivo(nombrearchivo, linea)
        guardar_archivo(nombrearchivo, array_contenido)
        print("Se creo el archivo ", nombrearchivo)
    else:
        return False

def guardar_archivo(nombrearchivo:str, contenido:list):
    with open(nombrearchivo, "w") as archivo:
        archivo.writelines(contenido)
    # archivo = open(nombrearchivo, "w+")
    # archivo.write(contenido)
    # archivo.close()

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
    return array
def objeto_a_csv(diccionario):
    array = []
    for clave in diccionario:
        array.append(str(diccionario[clave]))
    string = ",".join(array)
    return string