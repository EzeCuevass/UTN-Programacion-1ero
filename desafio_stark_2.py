from Package_Input import Input
from funciones_stark_2 import *

def menu():
    seguir = "si"
    while seguir == "si":
        print("""
A. Leer archivo JSON.
B. Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera
ascendente
C. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario.
D. Salir
""")
        opcion = Input.get_string("Elija una opcion: ")
        match opcion:
            case "A":
                print("Opcion A")
                heroes = leer_json("data_stark.json", "heroes")
                print(heroes)
            case "B":
                print("Opcion B")
                heroes = leer_json("data_stark.json", "heroes")
                print(ordenar_por_clave(heroes, "nombre"))
            case "C":
                print("Opcion C")
                heroes = leer_json("data_stark.json", "heroes")
                lista_ordenada = ordenar_por_clave(heroes, "nombre")
                generar_csv("nombre.csv", lista_ordenada)
            case "D":
                print("Adios!")
                seguir = "no"
            case _:
                print("Opcion invalida, intente otra vez")
menu()