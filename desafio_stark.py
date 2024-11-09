from Package_Input import Input
from data_stark import lista_personajes
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
    8. Salir
        """)
        opcion = Input.get_int("Elija su opcion: ", min=1, max= 8)
        match opcion:
            case 1:
                ordenar_por_clave(lista_personajes, "nombre", 1)
            case 2:
                filtrado = filtrar_por_clave(lista_personajes, "genero", "M")
                posicion = (obtener_min_max_por_clave(filtrado, "fuerza", opcion=-1))
                print(f"El superheroe mas debil es: {filtrado[posicion]['nombre']}")
            case 3:
                set_ojos = obtener_set_valores(lista_personajes, "color_ojos")
                for color in set_ojos:
                    cantidad = contador_valor(lista_personajes, "color_ojos", color)
                    print(f"Hay {cantidad} de heroes con el color de ojos {color}")
            case 4:
                set_pelos = obtener_set_valores(lista_personajes, "color_pelo")
                for color in set_pelos:
                    filtro = filtrar_por_clave(lista_personajes, "color_pelo", color)
                    print(f"Superheroes de color de pelo {color}:")
                    mostrar_objetos_array(filtro)
                    print("-------------------------------------")
            case 5:
                set_inteligencias = obtener_set_valores(lista_personajes, "inteligencia")
                for tipo in set_inteligencias:
                    filtro = filtrar_por_clave(lista_personajes, "inteligencia", tipo)
                    print(f"Superheroes de inteligencia {tipo}:")
                    mostrar_objetos_array(filtro)
                    print("-------------------------------------")
            case 6:
                fem = filtrar_por_clave(lista_personajes,"genero", "F")
                promedio_fem = promedio_por_clave(fem, "fuerza")
                mayor_al_promedio = []
                for heroe in lista_personajes:
                    if int(heroe["fuerza"]) > promedio_fem:
                        mayor_al_promedio.append(heroe)
                print("Los superheroes que tienen mayor fuerza al promedio son: \n")
                mostrar_objetos_array(mayor_al_promedio)
            case 7:
                for heroe in lista_personajes:
                    print(heroe["altura"])
                    print()
                    imc = float(heroe["peso"]) / ((float(heroe["altura"])/100)**2)
                    agregar_clave(heroe, "imc", imc)
                mostrar_objetos_array(lista_personajes)
            case 8:
                print("adios!")
                seguir = "no"
menu()