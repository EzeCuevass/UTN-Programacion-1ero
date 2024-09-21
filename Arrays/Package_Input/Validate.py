def validate_number_int(mensaje,mensaje_error,min,max,reintentos)->int:
    contador_intentos = 0
    numero = int(input(mensaje))
    while numero < min or numero > max:
        contador_intentos += 1
        numero = int(input(mensaje_error))
        if contador_intentos == reintentos:
            print("Intentos agotados. Intente mas tarde")
            return None
    return numero
def validate_number_float(mensaje,mensaje_error,min,max,reintentos)->float:
    contador_intentos = 0
    numero = float(input(mensaje))
    while numero < min or numero > max:
        contador_intentos += 1
        numero = float(input(mensaje_error))
        if contador_intentos == reintentos:
            print("Intentos agotados. Intente mas tarde")
            return None
    return numero
def validate_string(mensaje, mensaje_error, limite)->str:
    string = input(mensaje)
    while len(string) > limite:
        string = input(mensaje_error)
    return string