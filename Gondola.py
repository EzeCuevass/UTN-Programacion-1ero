from Package_Input import Input as i
productos = [
    [[],["Botellas",3,(0,1)],[],["Frascos",8,(0,3)],[]],
    [[],[],["Fideos", 2, (1,2)],[],[]],
    [[],[],[],["Leche",5,(2,3)],[]]
]
def menu_opciones():
    seguir = "si"
    def agregar(fila:int,columna:int,producto:list):
        productos[fila][columna] = producto
    def borrar(fila:int,columna:int):
        productos[fila][columna] = []
    def modificar(fila:int,columna:int,cantidad:int):
        productos[fila][columna][1] = cantidad
    def listar():
        print("Productos: ")
        for fila in productos:
            for columna in fila:
                if columna != []:
                    print(f"{columna[0]}: {columna[1]} unidades")
    def listar_orden():
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
    while seguir == "si":
        print("Bienvenido al control de stock!")
        print("""
                1-Alta de productos (producto nuevo)
                2-Baja de productos (producto existente)
                3-Modificar productos
                4-Listar productos
                5-Lista de productos ordenado por nombre
                6-Salir
            """)
        opcion = i.get_int("Que tarea desea realizar?: ", "Error, opcion invalida: ", 1, 6)
        match opcion:
            case 1:
                fila = i.get_int("Ingrese fila: ", min= 0, max= 2)
                columna = i.get_int("Ingrese columna: ", min=0, max=4)
                producto = [i.get_string("Ingrese el nombre del producto: "), i.get_int("Ingrese la cantidad del producto: ", (fila,columna))]
                agregar(fila, columna, producto)
            case 2:
                fila = i.get_int("Ingrese fila: ", min= 0, max= 2)
                columna = i.get_int("Ingrese columna: ", min=0, max=4)
                borrar(fila,columna)
            case 3:
                fila = i.get_int("Ingrese fila: ", min= 0, max= 2)
                columna = i.get_int("Ingrese columna: ", min=0, max=4)
                cantidad = i.get_int("Ingrese cantidad: ")
                modificar(fila,columna,cantidad)
            case 4:
                listar()
            case 5:
                listar_orden()
            case 6: 
                salir()
menu_opciones()