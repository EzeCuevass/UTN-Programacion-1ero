from Package_Input import Input
from funciones_practica import *
pacientes = []

def menu_opciones():
    """
    Menu de opciones para gestion de pacientes en una clinica
    """
    seguir = "si"
    while seguir == "si":
        print("""
    Sistema de Gestion de Clinica
    1: Cargar pacientes
    2: Mostrar todos los pacientes
    3: Buscar pacientes por numero de Historia clinica
    4: Ordenar pacientes por numero de Historia Clinica
    5: Mostrar paciente con mas dias de internacion
    6: Mostrar paciente con menos dias de internacion
    7: Pacientes internados mas de 5 dias
    8: Cantidad de pacientes internados mas de 5 dias
    9: Promedio de dias de internacion de todos los pacientes
    10: Salir
          """)
        opcion = Input.get_int("Ingrese la opcion que desea: ", min=1,max=10)
        match opcion:
            case 1:
                cargar_paciente(pacientes)
            case 2:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    mostrar_pacientes(pacientes)
            case 3:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    historia_clinica = Input.get_int("Ingrese el numero de historia clinica del paciente a buscar: ", min=0)
                    buscar_historia_clinica(pacientes,historia_clinica)
            case 4:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    ordenar_pacientes(pacientes)
            case 5:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    mas_dias_internado(pacientes)
            case 6:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    menos_dias_internado(pacientes)
            case 7:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    internado_5(pacientes)
            case 8:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    cantidad_pacientes_5_dias(pacientes)
            case 9:
                if pacientes == []:
                    print("No hay ningun paciente registrado: ")
                else:
                    promedio_internaciones(pacientes)
            case 10:
                seguir = "no"
menu_opciones()