def mostrar_lista(lista:list):
    """
    Funcion desarrollada para mostrar una lista.
    """
    for i in lista:
        print(i)
def swapear(lista:list,i:int,j:int):
    """
    Funcion para swapear, en el metodo de ordenamiento de burbujeo.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
def ordenar_ascendente(lista:list):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                swapear(lista,i,j)
def ordenar_descendente(lista:list):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:
                swapear(lista,i,j)
