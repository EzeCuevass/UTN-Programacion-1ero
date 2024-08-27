# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base, 
# se pide el ingreso de una estación del año(Invierno/Verano/Otoño/Primavera) y 
# localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) para vacacionar para poder 
# calcular el precio final: 
# -en Invierno: 
    # Bariloche tiene un aumento del 20% 
    # Cataratas y Córdoba tiene un descuento del 10% 
    # Mar del Plata tiene un descuento del 20% 
# -en Verano: 
    # Bariloche tiene un descuento del 20% 
    # Cataratas y Córdoba tiene un aumento del 10% 
    # Mar del Plata tiene un aumento del 20% 
#-en Otoño y Primavera: 
    # Bariloche tiene un aumento del 10% 
    # Cataratas tiene un aumento del 10% 
    # Mar del Plata tiene un aumento del 10% 
    # Córdoba tiene el precio sin descuento.
# Validar el ingreso de datos.

estadia_base = 15000
precio_final = 0
estacion = input("Ingrese la estacion del año en la cual quiere su estadia: ")
localidad = input("Ingrese la localidad donde quiere viajar: ")

if estacion == "Invierno":
    if localidad == "Bariloche":
        precio_final = estadia_base * 1.20
    elif estacion == "Mar del Plata":
        precio_final = estadia_base - (estadia_base * 0.20)
    else:
        precio_final = estadia_base - (estadia_base * 0.10)
elif estacion == "Verano":
    if localidad == "Bariloche":
        precio_final = estadia_base - (estadia_base * 0.20)
    elif estacion == "Mar del Plata":
        precio_final = estadia_base * 1.20
    else:
        precio_final = estadia_base * 1.10
else:
    if localidad == "Bariloche":
        precio_final = estadia_base * 1.10
    elif localidad == "Cataratas":
        precio_final = estadia_base * 1.10
    elif localidad == "Mar del Plata":
        precio_final = estadia_base * 1.10
    else:
        precio_final = precio_final

print(precio_final)