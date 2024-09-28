def agregar(productos,fila:int,columna:int,producto:list):
        productos[fila][columna] = producto
def borrar(productos,fila:int,columna:int):
    productos[fila][columna] = []
def modificar(productos,fila:int,columna:int,cantidad:int):
    productos[fila][columna][1] = cantidad
def listar(productos):
    print("Productos: ")
    for fila in productos:
        for columna in fila:
            if columna != []:
                print(f"{columna[0]}: {columna[1]} unidades")
def listar_orden(productos,):
    print("Productos: ")
    ordenados = []
    for fila in productos:
        for columna in fila:
            if columna != []:
                ordenados.append(columna[0])
    ordenados.sort()
    for producto in ordenados:
        print(producto)
def salir():
    seguir = "no"
