from .funciones import *
from Package_Input import Input as i
def menu_opciones(productos):
    seguir = "si"
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
                agregar(productos,fila, columna, producto)
            case 2:
                fila = i.get_int("Ingrese fila: ", min= 0, max= 2)
                columna = i.get_int("Ingrese columna: ", min=0, max=4)
                borrar(productos,fila,columna)
            case 3:
                fila = i.get_int("Ingrese fila: ", min= 0, max= 2)
                columna = i.get_int("Ingrese columna: ", min=0, max=4)
                cantidad = i.get_int("Ingrese cantidad: ")
                modificar(productos,fila,columna,cantidad)
            case 4:
                listar(productos)
            case 5:
                listar_orden(productos)
            case 6: 
                break