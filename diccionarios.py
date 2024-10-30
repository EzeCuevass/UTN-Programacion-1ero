from estudiantes import estudiantes
from Package_Input import Input
from Package_Lists import Lists
from funciones_diccionario import *
def menu():
    seguir = "si"
    while seguir == "si":
        print("""
1-Listar los alumnos por orden ascendente de apellido, si se repite,
ordenar por nombre. Mostrar legajo, nombre, apellido y edad
2-Obtener el promedio de notas para cada estudiante
3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el
programa de “Ingenieria en Informatica”
4-Obtener un promedio de edad de los estudiantes.
5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y
apellido
6-Listar nombre y apellido de los alumnos que forman el grupo “Club de
Informática” con sus respectivos promedios
7-Listar legajo, nombre, apellido y programas que cursan los alumnos
más jóvenes.
8- Salir.
              """)
        opcion = Input.get_int("Elige una opcion: ")
        match opcion:
            case 1:
                ordenar_ascendente_apellidos(estudiantes)
            case 2:
                obtener_promedio(estudiantes)
            case 3:
                obtener_ingenieros(estudiantes)
            case 4:
                promedio_edad(estudiantes)
            case 5:
                mayor_promedio(estudiantes)
            case 6:
                alumnos_club_informatica(estudiantes)
            
            case 8:
                seguir = "no"
menu()