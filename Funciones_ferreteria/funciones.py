def reponer(lista_estanteria,estanteria):
        lista_estanteria.append(estanteria)
        print("Estanteria repuesta!")
        # return lista_estanteria
def vender(lista_estanteria,fila:int,columna:int,cantidad:int):
    if lista_estanteria == []:
        print("No hay articulos cargados")
    else:
        if lista_estanteria[0][fila][columna][1] > cantidad:
            lista_estanteria[0][fila][columna][1] -= cantidad
        else:
            print("No hay stock suficiente, no se puede realizar la venta")
def listar(lista_estanteria):
    if lista_estanteria == []:
        print("No hay articulos cargados")
    else:
        print("Productos:")
        for fila in lista_estanteria[0]:
            for columna in fila:
                print(f"{columna[0]}: {columna[1]} unidades")
def salir():
    seguir = "no"