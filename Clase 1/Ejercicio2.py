# Ejercicio 2:
# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), 
# adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = int(input("Ingrese su edad: "))

if edad > 17:
    print("Usted es mayor de edad")
elif edad >= 13 and edad <= 17:
    print("Usted es adolescente")
else:
    print("Usted es niño")