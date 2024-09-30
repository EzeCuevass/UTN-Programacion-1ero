from .funciones import *
def menu():
    seguir = "si"
    while seguir == "si":
        print("""
    Menu de opciones:
    1:Importar listas
    2:Listar los datos de los usuarios de México
    3:Listar los nombre, mail y teléfono de los usuarios de Brasil
    4:Listar los datos del/los usuario/s más joven/es
    5:Obtener un promedio de edad de los usuarios
    6:De los usuarios de Brasil, listar los datos del usuario de mayor edad
    7:Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
    8:-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
    9: Cerrar menu
    """)
        opcion = int(input("Elija su opcion: "))
        match opcion:
            case 1:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    importar()
                    print("Listas importadas!")
            case 2:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    datos_mexico(pais[0])
            case 3:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    datos_brasil(pais[0])
            case 4:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    datos_jovenes(edad[0])
            case 5:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    promedio_edad(edad[0])
            case 6:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    datos_mayores(pais[0],edad[0])
            case 7:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    datos_8000(pais[0],codigo_postal[0])
            case 8:
                if direccion == [] and numero == [] and localidad == [] and pais == [] and edad == [] and nombre == [] and mail == [] and codigo_postal == []:
                    print("No se puede realizar las operaciones, no se importaron las listas.")
                else:
                    datos_italia_40(pais[0],edad[0])
            case 9:
                print("Adios!")
                break