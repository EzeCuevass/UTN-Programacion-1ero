# Ejercicio 1:
# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona.
nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))

sueldo_aumentado = sueldo * 1.10

print(f"Hola {nombre}! Tu sueldo con un 10% de aumento es {sueldo_aumentado}")