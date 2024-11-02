from Package_Input import Input
from Package_Lists import Lists
from data_stark import heroes
from stark_funciones import *
def menu():
    seguir = "si"
    while seguir == "si":
        print("""
    1. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por
    Nombre de manera ascendente.
    2. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de
    género M.
    3. Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de
    ojos.
    4. Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo.
    5. Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
    6. Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
    género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género
    femenino
    7. Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un
    nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el
    IMC calculado.
        """)
        opcion = Input.get_int("Elija su opcion: ", min=1, max= 7)
        match opcion:
            case 1:
                ordenar_por_nombre(heroes)
            case 2:
                superheroe_mas_debil(heroes)
            case 3:
                print("No se obtuvieron datos sobre los ojos.")
            case 4:
                print("No se obtuvieron datos sobre el pelo.")
            case 5:
                separar_inteligencia(heroes)
            case 6:
                print("No se tienen datos sobre generos.")
            case 7:
                calcular_imc(heroes)
menu()