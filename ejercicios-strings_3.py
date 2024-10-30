from Package_Lists import Lists
# Desarrollar una función que Invierte el orden de los caracteres en una cadena.

# def revertir(string:str) ->  str:
#     return string[::-1]
# print(revertir("anashe"))

# Desarrollar una función que cuente cuántas palabras hay en una cadena.

# def contar_palabras(string:str) -> str:
#     palabras = string.count(" ")+1
#     return palabras
# print(contar_palabras("River es lo mas grande que hay"))

# Desarrollar una función que reemplaza una palabra específica por otra en una cadena.

# def reemplazar_palabra(string:str, palabra:str, nueva:str) -> str:
#     return string.replace(palabra,nueva)
# print(reemplazar_palabra("Aguante River", "River", "Chicago"))


# Desarrollar una función que convierta los elementos de lista_peli en una
# cadena y muestre: 

# lista_peli = [
#     ["Matrix", "El Padrino", "Titanic"],
#     ["Forrest Gump", "Pulp Fiction", "Gladiador"],
#     ["Blade Runner", "El Rey León", "Volver al Futuro"],
#     ["La La Land", "El Gran Lebowski", "Blade Runner"],
#     ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
#     ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
#     ["Titanic", "Star Wars", "El Señor de los Anillos"],
#     ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
#     ["Forrest Gump", "The Godfather", "Goodfellas"],
#     ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
# ]
# for fila in lista_peli:
#     print(f'Se recomienda ver "{fila[0]}", "{fila[1]}" y "{fila[2]}"')

# Desarrollar una función que capitalice palabras en una cadena.

# def capitalizar_string(string:str) -> str:
#     palabras = string.split()
#     string_nuevo = ""
#     for i in range(len(palabras)):
#         palabras[i] = palabras[i].capitalize()
#     string_nuevo = " ".join(palabras)
#     return string_nuevo
# print(capitalizar_string("hola mundo"))

# Desarrollar una función que verifique si una cadena es un palíndromo:
# Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta
# la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo,
# anilina.

# def revertir(string:str) ->  str:
#     return string[::-1]

# def verificar_palindromo(string:str) -> bool:
#     palabra_invertida = revertir(string)
#     if palabra_invertida == string:
#         return True
#     else:
#         return False

# print(verificar_palindromo("anilina"))

# Desarrollar una función “ordenar” que recibe un string y un número (1 o -1). Se debe retornar el string 
# ordenado de manera ascendente (si recibió 1 por parámetros) o descendente (si recibió -1)
# Nota: Determinar parámetros y retornos de manera que las funciones sean genéricas y reutilizables.

def ordenar(string:str,numero:int) -> str:
    string = list(string)
    if numero == 1:
        Lists.ordenar_ascendente(string)
    elif numero == -1:
        Lists.ordenar_descendente(string)
    nuevostring = "" 
    nuevostring = "".join(string)
    return nuevostring
print(ordenar("A veces la vida es god y a veces la vida es zzz", -1))