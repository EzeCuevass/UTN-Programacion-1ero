# Mostrar los números ascendentes desde el 1 al 10
# for i in range(10):
#     print(i+1)
# Mostrar los números descendentes desde el 10 al 1
# for i in range(10):
#     print(10-i)
# Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
# numero = int(input("Ingresa un numero positivo: "))
# for i in range(numero):
#     print(i)
# Ingresar un número y mostrar la tabla de multiplicar de ese número
# numero = int(input("Ingresa un numero positivo: "))
# for i in range(1,11):
#     print(f"{numero}x{i} = {i*numero}")
# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
# Mostrar la suma y el promedio de todos los números.
# acumulador = 0
# promedio = 0
# for i in range(10):
#     numero = int(input("Ingresa un numero (Si es 0 se detiene el programa): "))
#     if numero == 0:
#         break
#     acumulador += numero
#     promedio = acumulador / (i+1)

# print(f"Suma: {acumulador}")
# print(f"Promedio: {promedio}")
# Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
# for i in range(1,11):
#     if i % 3 == 0:
#         print(i)
# Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)
# Realizar un programa que permita mostrar una pirámide de números. 
# numero = int(input("Ingrese un numero positivo para mostrar una piramide de numeros: "))
# string_num = ""
# for i in range(1,numero+1):
#     string_num += str(i)
#     print(string_num)
# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
# el número ingresado. Mostrar la cantidad de divisores encontrados.
# numero = int(input("Ingrese un numero positivo: "))
# contador_divisores = 0
# for i in range(1,numero+1):
#     if numero % i == 0:
#         print(i)
#         contador_divisores += 1
# print(f"Hay un total de {contador_divisores} divisores")
# Ingresar un número. Determinar si el número es primo o no.
# numero = int(input("Ingrese un numero positivo: "))
# contador_divisores = 0
# for i in range(1,numero+1):
#     if numero % i == 0:
#         contador_divisores += 1
# if contador_divisores > 2:
#     print(f"{numero} no es primo")
# else:
#     print(f"{numero} es primo")
# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
# número ingresado. Informar cuántos números primos se encontraron.
# numero = int(input("Ingrese un numero positivo: "))
# contador_divisores = 0
# contador_primos = 0
# for i in range(1,numero+1):
#     for num in range(1,i):
#         if num % i == 0:
#             contador_divisores += 1
#         if contador_divisores <= 2:
#             contador_primos += 1
#             print(num)
# print(f"Se encontraron {contador_primos} numeros primos entre el 1 y el {numero}")