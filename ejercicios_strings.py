from Package_Input import Input
# Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
# Debe retornar las veces que la letra está incluida en el texto.

# def buscar_caracter(letra:str,texto:str)->int:
#     f"""
#     Lo que hace la funcion es buscar el caracter pasado por parametro ({letra}) en el texto pasado por parametro ({texto}).
#     """
#     veces_en_texto = 0
#     for caracter in texto.lower():
#         if caracter == letra.lower():
#             veces_en_texto += 1
#     return veces_en_texto

# print(buscar_caracter(Input.get_string("Ingrese la letra a ser buscada: ", limite=1), Input.get_string("Ingrese el texto en el que se va a buscar esa letra: ")))

# Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
# Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
# Si las posiciones no son válidas se debe informar.
# no entendi

# Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
# **IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
# <número de caracteres> - 1.

# def char_at()->str:
#     """
#     La funcion char_at, pide un texto, y el numero del caracter que quiere retornar.
#     """
#     texto = Input.get_string("Ingrese un texto: ")
#     numero = Input.get_int("Ingrese el numero del caracter que quiere: ") - 1 
    
#     return texto[numero]
# print(char_at())