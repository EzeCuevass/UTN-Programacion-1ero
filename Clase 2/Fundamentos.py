contador_hombres_iot_ia_25_50 = 0
ingresos = 0
contador_not_f_not_ia_33_40 = 0
nombre_max = ""
tecnologia_max = ""
edad_max = 0 
for i in range(10):
    # Ingreso de datos
    nombre = input("Nombre del empleado?: ")
    edad = int(input("Edad del empleado?: "))
    while edad < 18:
        edad = int(input("Error. Ingrese nuevamente. Edad del empleado?: "))
    genero = input("Genero del empleado?: ").lower()
    while genero != "masculino" and genero != "femenino" and  genero != "otro":
        genero = input("-Error. Ingrese nuevamente. Genero del empleado?: ")
    tecnologia = input("Tecnologia (IA, RV/RA, IOT): ").lower()
    while tecnologia != "ia" and tecnologia != "rv/ra" and tecnologia != "iot":
        tecnologia = input("Error. Ingrese nuevamente. Tecnologia (IA, RV/RA, IOT): ").lower()
        ingresos += 1
    # Logica
    if genero == "masculino" and (edad >= 25 and edad <=50) and (tecnologia == "iot" or tecnologia == "ia"):
        contador_hombres_iot_ia_25_50 += 1
    if tecnologia != "ia" and (genero != "femenino" or (edad >= 33 and edad <= 40)):
        contador_not_f_not_ia_33_40 += 1
    if edad > edad_max:
        if genero == "masculino":
            nombre_max = nombre
            edad_max = edad
            tecnologia_max = tecnologia.upper()
print(contador_hombres_iot_ia_25_50)
print(contador_not_f_not_ia_33_40)
print(f"El empleado {nombre} voto {tecnologia_max}")