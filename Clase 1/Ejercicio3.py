# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

ingresos = 0
contador_pares = 0
contador_impares = 0
minimo = 0
maximo_pares = 0
suma_positivos = 0
contador_negativos = 0
contador_positivos = 0
producto_negativos = 1
ingresos_pares = 0
for i in range(5):

    numero = int(input("Ingrese un numero (Distinto de 0): "))
    while numero == 0:
        numero = int(input("Error. Ingrese un numero nuevamente:"))
    
    if ingresos == 0:
        minimo = numero
    
    if numero % 2 == 0:
        contador_pares += 1
        if ingresos_pares == 0:
            maximo_pares = numero
        if maximo_pares < numero:
            maximo_pares = numero
    else:
        contador_impares += 1

    if minimo > numero:
        minimo = numero
    
    if numero > 0:
        contador_positivos += 1
        suma_positivos += numero
    else:
        contador_negativos += 1
        producto_negativos = producto_negativos * numero
    
    ingresos += 1


print(f"La cantidad de numeros impares es de {contador_impares}")
print(f"La cantidad de numeros pares es de {contador_pares}")
print(f"El menor numero ingresado es {minimo}")
if contador_pares == 0: 
    print("No se ingresaron numeros pares")
else:
    print(f"De los pares, el mayor numero ingresado es {maximo_pares}")
    
if contador_positivos > 0:
    print(f"La suma de los positivos es de {suma_positivos}")
else:
    print("No se ingresaron numeros positivos")
if contador_negativos > 0:
    print(f"El producto de los negativos es de {producto_negativos}")
else:
    print("No se ingresaron numeros negativos")