continuar = "Si"
contador_elite_plano_19_25 = 0
ingresos_50 = 0
menor_50 = 60
nombre_menor_50 = ""
categoria_menor_50 = ""
ingresos = 0
contador_experto = 0
acumulador_edad_avanzado = 0
contador_avanzado = 0
contador_elite_plano = 0
contador_elite_liftado = 0
contador_elite_cortado = 0

while continuar == "Si":
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador (No puede ser menor a 18 años, limite 60 años): "))
    while edad < 18 or edad > 60:
        edad = int(input("Error. Ingrese nuevamente la edad del jugador (No puede ser menor a 18 años, limite 60 años): "))
    puntos = int(input("Ingrese la cantidad de puntos del jugador (Limite: 60): "))
    while puntos < -1 or puntos > 61:
        puntos = int(input("Error. Ingrese nuevamente la cantidad de puntos del jugador (Limite: 60): "))
    partidos_ganados = int(input("Ingrese la cantidad de partidos ganados del jugador (Limite: 35): "))
    while partidos_ganados < -1 or partidos_ganados > 35:
        partidos_ganados = int(input("Error. Ingrese nuevamente la cantidad de partidos ganados del jugador (Limite: 35): "))
    saque = input("Ingrese el tipo de saque del jugador (Plano, Liftado, Cortado): ").lower()
    while saque != "plano" and saque != "liftado" and saque != "cortado":
        saque = input("Error. Ingrese nuevamente el tipo de saque del jugador (Plano, Liftado, Cortado): ").lower()
    categoria = input("Ingrese la categoria del jugador (Elite, Experto, Avanzado): ").lower()
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Error. Ingrese nuevamente la categoria del jugador (Elite, Experto, Avanzado): ").lower()
    
    ingresos += 1
    
    if puntos > 50:
        if menor_50 > edad:
            menor_50 = edad
            nombre_menor_50 = nombre
            categoria_menor_50 = categoria

    if categoria == "experto":
        contador_experto += 1
    
    if categoria == "avanzado":
        acumulador_edad_avanzado += edad
        contador_avanzado += 1
    
    if categoria == "elite":
        if (edad >= 19 and edad <= 25) and saque == "plano":
            contador_elite_plano_19_25 += 1
        if saque == "plano":
            contador_elite_plano += 1
        if saque == "liftado":
            contador_elite_liftado += 1
        if saque == "cortado":
            contador_elite_cortado += 1

    continuar = input("Ingrese 'Si' para continuar: ")

# 1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
# inclusive

print(f"Hay {contador_elite_plano_19_25} jugadores de la categoria Elite, con saque Plano de entre 19 y 25 años")
# 2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
print(f"El jugador {nombre_menor_50}, de la categoria {categoria_menor_50}, fue el mas joven en obtener 50 puntos")
# 3-Porcentaje de jugadores de categoría "experto".
if contador_experto > 0:
    porcentaje = contador_experto * 100 / ingresos
    print(f"El porcentaje de jugadores expertos es de : {porcentaje}")
else:
    print("No se obtuvieron datos de jugadores de la categoria Experto")
# 4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”
if contador_avanzado > 0:
    promedio_avanzado = acumulador_edad_avanzado / contador_avanzado
    print(f"El promedio de edad de los jugadores de categoria 'Avanzado' es de {promedio_avanzado}")
else:
    print("No se obtuvieron datos de jugadores de la categoria Avanzado")
# 5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.

if contador_elite_plano > contador_elite_liftado and  contador_elite_plano > contador_elite_cortado:
    print("El saque mas usado por los jugadores de elite es el saque plano")
elif contador_elite_liftado > contador_elite_cortado:
    print("El saque mas usado por los jugadores de elite es el saque liftado")
elif contador_elite_cortado > contador_elite_liftado:
    print("El saque mas usado por los jugadores de elite es el saque cortado")
else:
    print("Ningun saque predomina entre los jugadores de elite")