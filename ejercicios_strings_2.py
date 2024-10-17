from Package_Input import Input
from Package_Lists import Lists
# Crear una función que reciba como parámetro una cadena y determine la
# cantidad de vocales que hay de cada una (individualmente). La función
# retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
# la cantidad.

# def analizar_cadena(string:str)->list:
#     matriz = [
#         ["a",0],["e",0],["i",0],["o",0],["u",0]
#     ]
#     for caracter in string:
#         if caracter == matriz[0][0]:
#             matriz[0][1] += 1
#         elif caracter == matriz[1][0]:
#             matriz[1][1] += 1
#         elif caracter == matriz[2][0]:
#             matriz[2][1] += 1
#         elif caracter == matriz[3][0]:
#             matriz[3][1] += 1
#         elif caracter == matriz[4][0]:
#             matriz[4][1] += 1
#     return matriz
# Lists.mostrar_matriz(analizar_cadena(Input.get_string("Introduce un string a analizar: ").lower()))

# Crear una función que reciba una cadena y un caracter. La función deberá
# devolver el índice en el que se encuentre la primera incidencia de dicho
# caracter, o -1 en caso de que no esté.

# def analizar_string(string:str,char:str)->int:
#     index = range(len(string))
#     string = string.lower()
#     posicion = -1
#     for caracter in string:
#         for i in index:
#             if string[i] == char:
#                 posicion = index[i]
#                 break
#     return posicion

# print(analizar_string("Roberto Carlos","r"))

# Crear una función que reciba como parámetro una cadena y suprima los
# caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def eliminar_repetidos(string:str)->str:
    index = range(len(string))
    for caracter in string:
        for i in index:
            print(i)
            if string[i] == string[i+1]:
                string.splice(i,1)
    return string
print(eliminar_repetidos("GOOOOD"))