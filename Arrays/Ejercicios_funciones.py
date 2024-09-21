from Package_Input import Input as PI
# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los guarde en una lista y la 
# retorne. El programa principal debe invocar a la función y mostrar por pantalla el retorno.
# def agregar_nombres():
#     nombres = []
#     for i in range(10):
#         nombre = input("Ingrese un nombre a ingresar en la lista: ")
#         nombres.append(nombre)
#     return nombres
# print(agregar_nombres())
# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida posición y número a 
# guardar al usuario, lo guarde en una lista en la posición solicitada aleatoriamente y la retorne. 
# El programa principal debe invocar a la función y mostrar por pantalla el retorno.
# def lista_0():
#     lista = []
#     for i in range(10):
#         lista.append(0)
#     posicion = int(input("Ingrese la posicion a modificar de la lista: "))
#     numero = int(input("Ingrese el numero que quiere meter en la lista: "))
#     lista[posicion] = numero
#     return lista
# print(lista_0())
# Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango especificado, validar los 
# números solicitados dentro de ese rango, guardar en una lista y retornarla. El programa principal debe invocar 
# a la función y mostrar por pantalla el retorno
# def numero_a_lista()->list:
#     lista = list()
#     for i in range(10):
#         numero = PI.get_int("Ingrese un numero del 1 al 20: ", "Error. Intente otra vez: ", 1, 20)
#         lista.append(numero)
#     return lista
# print(numero_a_lista())
# Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números y un número especificado. 
# La misma debe buscar el número especificado en la lista y retornar “True” si existe.
# def buscar(lista:list,numero:int)->bool:
#     for i in range(len(lista)):
#         print(len(lista))
#         if lista[i] == numero:
#             return True
# Ejercicio 5: Dadas las siguientes listas:
# nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las
# personas de menor edad (puede ser más de una) y las retorne. El programa
# principal deberá mostrar nombre y edad de los menores.
# posiciones = []
# def buscar_menores(lista_edades:list):
#     menores = list()
#     # menores.append(edades[0])
#     for i in range(len(edades)):
#         if i == 0 or (edades[i] < menores[0]):
#             menores = [edades[i]]
#             posiciones = [i]
#         elif edades[i] == menores[0]:
#             menores.append(edades[i])
#             posiciones.append(i)
#             print(posiciones)
#     return posiciones
# array_menores = buscar_menores(edades)
# if len(array_menores) > 1:
#     print(f"Hay {len(array_menores)} personas que comparten la caracteristica de tener la menor edad en la lista")
# else:
#     print("Solo hay una persona que tiene la menor edad en la lista.")
# print(array_menores)
# for i in range(len(array_menores)):
#     print(f"{nombres[array_menores[i]]} con {edades[array_menores[i]]}")
# Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo listas_personas.py. 
# Importar los nombres a una lista. Realizar una función que muestre los mismos.
# from listas_personas import nombres
# lista_nombres = list(nombres)
# def mostrar(lista):
#     for i in range(len(lista)):
#         print(lista[i])
# mostrar(lista_nombres)
# Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de compras on-line 
# recientemente lanzado al mercado para ello necesita un programa que le permita acceder a los datos relevados.
# def menu():
#     print("""
#             Menu de opciones:
#             1:Importar listas
#             2:Listar los datos de los usuarios de México
#             3:Listar los nombre, mail y teléfono de los usuarios de Brasil
#             4:Listar los datos del/los usuario/s más joven/es
#             5:Obtener un promedio de edad de los usuarios
#             6:De los usuarios de Brasil, listar los datos del usuario de mayor edad
#             7:Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000
#             8:-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
# años.
#             9: Cerrar menu
# """)
#     opcion = int(input("Elija su opcion: "))
#     posicion = []
#     while opcion != 9:
#         if opcion == 1:
#             from listas_personas import address, telefonos, region, country, edades, mails, nombres, postalZip
#             opcion = ("Elija su opcion: ")
#             print("Listas importadas!")
#         if opcion == 2:
#             for i in range(len(country)):
#                 if country[i] == "Mexico":
#                     print(posicion)
# menu()