from Validate import *
def get_int(mensaje="Ingrese un numero entero: ",mensaje_error="Error, intente otra vez: ",min=float('-inf'),max=float('+inf'),reintentos=float('+inf'))->int|None:
    numero = validate_number_int(mensaje,mensaje_error,min,max,reintentos)
    return numero

def get_float(mensaje="Ingrese un numero flotante: ",mensaje_error="Error, intente otra vez: ",min=float('-inf'),max=float('+inf'),reintentos=float('+inf'))->int|None:
    numero = validate_number_float(mensaje,mensaje_error, min, max, reintentos)
    return numero

def get_string(mensaje, mensaje_error="Limite de caracteres alcanzado. Intente otra vez: ", limite=float('+inf'))->str:
    string = validate_string(mensaje,mensaje_error, limite)
    return string
print(get_int("Ingrese un numero del 1 al 10: ", min=1, max= 10))
print(get_float("Ingrese un numero del 1 al 10: ", min=1, max= 10))
print(get_string("Ingrese un string (7 caracteres maximo): ", limite=7))