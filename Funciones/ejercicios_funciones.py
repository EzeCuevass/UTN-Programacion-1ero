# Crear una función que muestre por pantalla el número que recibe como parámetro.
# def funcion(numero):
#     print(f"El numero elegido es {numero}")
# funcion(int(input("Elige un numero: ")))
# Crear una función que pida el ingreso de un número y lo retorne.
# def funcion():
#     numero = int(input("Ingresa un numero: "))
#     return numero
# print(funcion())
# Crear una función que permita determinar si un número es par o no. La función retorna “True” en caso afirmativo y 
# “False" en caso contrario. Probar en el programa principal realizando la invocación o llamada.
# def par_o_no():
#     numero = int(input("Ingresa un numero: "))
#     if numero % 2 == 0:
#         return True
#     else: 
#         return False
# print(par_o_no())
# Especializar la función del punto 3.1 y 3.2 para que valide el número en
# un rango determinado pasado por parámetro “desde”-“hasta”.
# def en_rango(rango_1,rango_2,numero):
#     if numero >= rango_1 and numero <= rango_2:
#         return f"El numero {numero} esta en el rango comprendido entre {rango_1} y {rango_2}"
#     else:
#         return f"El numero {numero} NO esta en el rango comprendido entre {rango_1} y {rango_2}"
# rango_1 = int(input("Ingesa el numero mas pequeño del rango: "))
# rango_2 = int(input("Ingesa el numero mas grande del rango: "))
# numero =  int(input("Ingresa el numero a ser buscado en el rango: "))
# print(en_rango(rango_1,rango_2,numero))
# Realizar un programa en donde se puedan utilizar los prototipos de la
# función Restar en sus 4 combinaciones.

# Definitivamente no lo entendi

# Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario, valide el mismo entre 
# 10 y 100, realice un descuento del 5% a dicho valor a través de una función llamada realizarDescuento(). 
# Mostrar el resultadopor pantalla. Atención: pueden reutilizarse funciones ya creadas.

def en_rango(rango_1:int,rango_2:int,numero:int) -> bool:
    if (numero >= rango_1 and numero <= rango_2) or (numero >= rango_2 and numero <= rango_1):
        return True
    else:
        return False
rango_1 = int(input("Ingesa el primer numero del rango: "))
rango_2 = int(input("Ingesa el segundo numero del rango: "))
numero1 =  int(input("Ingresa el numero a ser buscado en el rango: "))
def realizarDescuento(numero1):
    descuento = 5/100
    if en_rango(rango_1,rango_2,numero1):
        return numero1 - (numero1 * descuento)  
    else:
        return numero1

print(realizarDescuento(numero1))

# Realizar un programa que: asigne a las variables numero1 y numero2 los valores solicitados al usuario, 
# valide los mismos entre 10 y 100, asigne a la variable operacion el valor solicitado al usuario: 
# 's'-sumar, 
# 'r'-restar (validar),
# realice la operación de dichos valores a través de una función. Mostrar el resultado por pantalla.

# def calculadora(numero1,numero2,operacion):
#     if operacion == "s":
#         return numero1 + numero2
#     else:
#         return numero1 - numero2
    
# numero1 = int(input("Ingrese un numero para operar: "))
# numero2 = int(input("Ingrese otro numero para operar: "))
# operacion = input("Que operacion va a hacer? 'S' para suma y 'R' para resta: ").lower()
# while operacion != "s" and operacion != "r":
#     operacion = input("Error. Ingrese nuevamente la operacion: ")

# print(calculadora(numero1,numero2,operacion))