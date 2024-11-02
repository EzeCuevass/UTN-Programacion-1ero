from Package_Input import Input
from Package_Lists import Lists
def ordenar_ascendente_apellidos(estudiantes:list) -> None:
    """
    Listar los alumnos por orden ascendente de apellido, si se repite,
    ordenar por nombre. Mostrar legajo, nombre, apellido y edad    
    """
    for i in range(len(estudiantes)):
        for j in range(i, len(estudiantes)):
            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"]:
                aux = estudiantes[j]["apellido"]
                estudiantes[j]["apellido"] = estudiantes[i]["apellido"]
                estudiantes[i]["apellido"] = aux
            elif estudiantes[i]["apellido"] == estudiantes[j]["apellido"]:
                if estudiantes[i]["nombre"] > estudiantes[j]["nombre"]:
                    aux = estudiantes[j]["nombre"]
                    estudiantes[j]["nombre"] = estudiantes[i]["nombre"]
                    estudiantes[i]["nombre"] = aux
    for estudiante in estudiantes:
        print(f"Apellido: {estudiante['apellido']}" )
        print(f"Nombre: {estudiante['nombre']}" )
        print(f"Legajo: {estudiante['legajo']}" )
        print(f"Edad: {estudiante['edad']}" )
def obtener_promedio(estudiantes:list) -> None:
    """
    Obtener el promedio de notas para cada estudiante
    """
    for estudiante in estudiantes:
        notas_totales = 0
        notas_acumulador = 0
        for nota in estudiante["notas"]:
            notas_totales+=1
            notas_acumulador+= nota
        promedio = notas_acumulador / notas_totales
        print(f"El promedio de {estudiante['apellido']} {estudiante['nombre']} es de {promedio}")
def obtener_ingenieros(estudiantes:list) -> None:
    """
    Listar legajo, nombre, apellido y edad de los estudiantes que cursan el
    programa de “Ingenieria en Informatica”
    """
    for estudiante in estudiantes:
        if estudiante["programa"]["nombre"] == "Ingenieria en Informatica":
            print(f'Legajo: {estudiante["legajo"]}')
            print(f'Nombre: {estudiante["nombre"]}')
            print(f'Apellido: {estudiante["apellido"]}')
            print(f'Edad: {estudiante["edad"]}')
def promedio_edad(estudiantes:list) -> None:
    """
    Obtener un promedio de edad de los estudiantes.
    """
    acumulador_edad = 0
    for estudiante in estudiantes:
        acumulador_edad += estudiante["edad"]
    total_estudiantes = len(estudiantes)
    promedio_edad = acumulador_edad / total_estudiantes
    print(f"El promedio de edad de los estudiantes es de {promedio_edad}")
def mayor_promedio(estudiantes:list) -> None:
    """
    Informar el alumno con mayor promedio de notas. Mostrar nombre y
    apellido
    """
    mayor = 0
    bandera = True
    posicion = 0
    for i in range(len(estudiantes)):
        notas_acumulador = 0
        for nota in estudiantes[i]["notas"]:
            notas_acumulador += nota
        promedio = notas_acumulador / len(estudiantes[i]["notas"])
        if promedio > mayor or bandera:
            mayor = promedio
            bandera = False
            posicion = i
    mejor_promedio = estudiantes[posicion]
    print(f"El estudiante con mejor promedio es {mejor_promedio['apellido']} {mejor_promedio['nombre']}")
def alumnos_club_informatica(estudiantes:list) -> None:
    """
    Listar nombre y apellido de los alumnos que forman el grupo “Club de
    Informática” con sus respectivos promedios
    """
    posiciones = []
    for i in range(len(estudiantes)):
        for grupo in estudiantes[i]["grupos"]:
            if grupo == "Club de Informatica":
                posiciones.append(i)
    print("Integrantes del Club de informatica:")
    for posicion in posiciones:
        notas_acumulador = 0
        for nota in estudiantes[posicion]['notas']:
            notas_acumulador += nota
        promedio = notas_acumulador / len(estudiantes[posicion]['notas'])
        print(f"{estudiantes[posicion]['nombre']} {estudiantes[posicion]['apellido']} con promedio de {promedio}")