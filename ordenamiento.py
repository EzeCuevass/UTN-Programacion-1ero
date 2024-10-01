from Package_Lists import Lists
# Ejercicio 1:
# Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.

# Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

# def ordenar_ascendente():
#     """
#     Funcion que ordena ascendentemente las listas en base a los Nombres, con el metodo de burbujeo, las modifica,
#     por lo cual no necesita parametros.
#     """
#     for i in range(len(Nombres)):
#         for j in range(i+1,len(Nombres)):
#             if Nombres[i] > Nombres[j]:
#                 Lists.swapear(Nombres,i,j)
#                 Lists.swapear(Edades,i,j)
# Lists.mostrar_lista(Nombres) #Lista antes de ser ordenada
# ordenar_ascendente()
# Lists.mostrar_lista(Nombres) #Lista despues de ser ordenada

# Ejercicio 2

# Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si 
# el nombre es el mismo, debe ordenar por puntos de manera descendente.
# Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
# Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]


# def ordenar_ascendente():
#     """
#     Funcion para ordenar ascendentemente la lista segun nombres, si es que hay nombres iguales, los ordena por puntos
#     de manera descendente.
#     """
#     for i in range(len(Nombres)):
#         for j in range(i+1, len(Nombres)):
#             if Nombres [i] > Nombres[j]:
#                 Lists.swapear(Nombres,i,j)
#                 Lists.swapear(Puntos,i,j)
#             elif Nombres[i] == Nombres[j]:
#                 if Puntos[i] < Puntos [j]:
#                     Lists.swapear(Nombres,i,j)
#                     Lists.swapear(Puntos,i,j)
# Lists.mostrar_lista(Nombres) #Lista antes del cambio
# ordenar_ascendente()
# Lists.mostrar_lista(Nombres) #Lista despues del cambio

# Ejercicio 3

# Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el apellido 
# es el mismo, debe ordenar por nombre de manera ascendente, si el nombre también es el mismo, debe ordenar por nota 
# de manera descendente.

Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos =["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_ascendente():
    """
    Funcion para ordenar ascendentemente la lista segun apellidos, si es que hay apellidos iguales, los ordena por 
    nombres de manera ascendente, si son iguales, los ordena por la nota ascendentemente.
    """
    for i in range(len(Apellidos)):
        for j in range(i+1, len(Apellidos)):
            if Apellidos [i] > Apellidos[j]:
                Lists.swapear(Apellidos,i,j)
                Lists.swapear(Estudiantes,i,j)
                Lists.swapear(Nota,i,j)
            elif Apellidos[i] == Apellidos[j]:
                if Estudiantes[i] > Estudiantes [j]:
                    Lists.swapear(Apellidos,i,j)
                    Lists.swapear(Estudiantes,i,j)
                    Lists.swapear(Nota,i,j)
                elif Estudiantes[i] == Estudiantes[j]:
                    if Nota[i] > Nota[j]:
                        Lists.swapear(Apellidos,i,j)
                        Lists.swapear(Estudiantes,i,j)
                        Lists.swapear(Nota,i,j)
Lists.mostrar_lista(Apellidos) #Lista antes del cambio
ordenar_ascendente()
Lists.mostrar_lista(Apellidos) #Lista despues del cambio