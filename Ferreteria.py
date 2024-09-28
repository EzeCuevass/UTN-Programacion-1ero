from Package_Input import Input as i
estanteria = [
    [["to12",65],["to16",86],["to20",65],["to25",45]],
    [["to30",68],["to35",73],["to40",85],["to45",89]],
    [["ta4",58],["ta5",48],["ta6",64],["ta7",96]],
    [["ta8",36],["ta10",72],["ta12",78],["ta14",71]]
]
def menu_opciones(estanteria):
    lista_estanteria = []
    seguir = "si"
    def reponer(estanteria):
        lista_estanteria.append(estanteria)
        print("Estanteria repuesta!")
        # return lista_estanteria
    def vender(fila:int,columna:int,cantidad:int):
        if lista_estanteria == []:
            print("No hay articulos cargados")
        if lista_estanteria[0][fila][columna][1] > cantidad:
            lista_estanteria[0][fila][columna][1] -= cantidad
        else:
            print("No hay stock suficiente, no se puede realizar la venta")
    def listar():
        print("Productos:")
        print(lista_estanteria[0])
        for fila in lista_estanteria[0]:
            for columna in fila:
                print(f"{columna[0]}: {columna[1]} unidades")
    def salir():
        seguir = "no"
    while seguir == "si":
        print("Bienvenido al control de stock!")
        print("""
1: Reponer mercaderia
2: Vender mercaderia (seleccionar fila y columna) 
3: Listar inventaria
4: Salir
""")
        opcion = i.get_int("Que tarea desea realizar?: ", "Error, opcion invalida: ", 1, 4)
        match opcion:
            case 1:
                reponer(estanteria)
            case 2:
                fila = i.get_int("Ingrese fila: ", min= 0, max= 2)
                columna = i.get_int("Ingrese columna: ", min=0, max=4)
                cantidad = i.get_int("Ingrese cantidad: ")
                vender(fila,columna,cantidad)
            case 3:
                listar()
            case 4:
                salir()
menu_opciones(estanteria)