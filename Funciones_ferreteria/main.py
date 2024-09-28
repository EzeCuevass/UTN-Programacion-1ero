from .funciones import *
from Package_Input import Input as i
def menu_opciones(estanteria):
    lista_estanteria = []
    seguir = "si"
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
                reponer(lista_estanteria,estanteria)
            case 2:
                fila = i.get_int("Ingrese fila: ", min= 0, max= 2)
                columna = i.get_int("Ingrese columna: ", min=0, max=4)
                cantidad = i.get_int("Ingrese cantidad: ")
                vender(lista_estanteria,fila,columna,cantidad)
            case 3:
                listar(lista_estanteria)
            case 4:
                break