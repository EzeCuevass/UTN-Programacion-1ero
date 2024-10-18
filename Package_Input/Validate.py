def validate_number_int(mensaje,mensaje_error,min,max,reintentos)->int:
    contador_intentos = 0
    numero = input(mensaje)
    def esentero(numero):
        if len(numero)>0:
            if numero[0] == "-":
                if len(numero) == 1:
                    return False
                for caracter in numero[1:]:
                    if not "0" <= caracter <= "9":
                        return False
            for caracter in numero:
                if not "0"<= caracter <= "9": 
                    return False
        else:
            return False
        return True
    while esentero(numero) == False or numero < min or numero > max:
        contador_intentos += 1
        numero = input(mensaje_error)
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