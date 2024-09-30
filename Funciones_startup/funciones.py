from .listas_personas import address, telefonos, region, country, edades, mails, nombres, postalZip
direccion = []
numero = []
localidad = []
pais = []
edad = []
mail = []
nombre = []
codigo_postal = []
def importar():
        direccion.append(address)
        numero.append(telefonos)
        localidad.append(region)
        pais.append(country)
        edad.append(edades)
        mail.append(mails)
        nombre.append(nombres)
        codigo_postal.append(postalZip)
def datos_mexico(country):
    posicion = []
    print("Datos de los usuarios de Mexico: ")
    for i in range(len(country)):
        if country[i] == "Mexico":
            posicion.append(i)
            mensaje = f"Nombre: {nombres[i]}\n"
            mensaje += f"Edad: {edades[i]}\n"
            mensaje += f"Mail: {mails[i]}\n"
            mensaje += f"Telefono: {telefonos[i]}\n"
            mensaje += f"Direccion: {address[i]}\n"
            mensaje += f"Pais: {country[i]}"
            mensaje += f"Region: {region[i]}\n"
            mensaje += f"Codigo postal: {postalZip[i]}\n"
            print(mensaje)
def datos_brasil(country):
    posicion = []
    print("Datos de los usuarios de Brasil:")
    for i in range(len(country)):
        if country[i] == "Brazil":
            posicion.append(i)
            mensaje = f"Nombre: {nombres[i]}\n"
            mensaje += f"Mail: {mails[i]}\n"
            mensaje += f"Edad : {edades[i]}\n"
            mensaje += f"Telefono: {telefonos[i]}\n"
            mensaje += f"Pais: {country[i]}\n"
            print(mensaje)
def datos_jovenes(edad):
    menores = []
    posicion = []
    for i in range(len(edad)):
        if i == 0 or edad[i] < menores[0]:
            menores = [edad[i]]
            posicion = [i]
        elif edad[i] == menores[0]:
            menores.append(edad[i])
            posicion.append(i)
    for i in posicion:
            mensaje = f"Nombre: {nombres[i]}\n"
            mensaje += f"Edad: {edades[i]}\n"
            mensaje += f"Mail: {mails[i]}\n"
            mensaje += f"Telefono: {telefonos[i]}\n"
            mensaje += f"Direccion: {address[i]}\n"
            mensaje += f"Pais: {country[i]}"
            mensaje += f"Region: {region[i]}\n"
            mensaje += f"Codigo postal: {postalZip[i]}\n"
            print(mensaje)
def promedio_edad(edad):
    acumulador = 0
    for i in edad:
        acumulador += i
    cantidad_edades = len(edad)
    promedio = acumulador / cantidad_edades
    print(f"El promedio de edad de los usuarios es de {promedio} años")
def datos_mayores(country, edad):
    posicion = []
    mayores = 0
    mensaje = ""
    for i in range(len(country)):
        if country[i] == "Brazil":
            posicion.append(i)
    for i in posicion:
        if edad[i] > mayores:
            mayores = edad[i]
            mensaje += f"Nombre: {nombres[i]}\n"
            mensaje += f"Edad: {edades[i]}\n"
            mensaje += f"Mail: {mails[i]}\n"
            mensaje += f"Telefono: {telefonos[i]}\n"
            mensaje += f"Direccion: {address[i]}\n"
            mensaje += f"Pais: {country[i]}\n"
            mensaje += f"Region: {region[i]}\n"
            mensaje += f"Codigo postal: {postalZip[i]}\n"
    print(mensaje)
def datos_8000(country,codigo):
    posicion = []
    for i in range(len(country)):
        if country[i] == "Brazil" or country[i] == "Mexico":
            if codigo[i] > 8000:
                posicion.append(i)
    for i in posicion:
            mensaje = f"Nombre: {nombres[i]}\n"
            mensaje += f"Edad: {edades[i]}\n"
            mensaje += f"Mail: {mails[i]}\n"
            mensaje += f"Telefono: {telefonos[i]}\n"
            mensaje += f"Direccion: {address[i]}\n"
            mensaje += f"Pais: {country[i]}\n"
            mensaje += f"Region: {region[i]}\n"
            mensaje += f"Codigo postal: {postalZip[i]}\n"
            print(mensaje)
def datos_italia_40(country,edad):
    posicion = []
    for i in range(len(country)):
        if country[i] == "Italy" and edad[i] > 40:
            posicion.append(i)
    for i in posicion:
        mensaje = f"Nombre: {nombres[i]}\n"
        mensaje += f"Edad: {edades[i]}\n"
        mensaje += f"Mail: {mails[i]}\n"
        mensaje += f"Telefono: {telefonos[i]}\n"
        mensaje += f"Direccion: {address[i]}\n"
        mensaje += f"Pais: {country[i]}\n"
        mensaje += f"Region: {region[i]}\n"
        mensaje += f"Codigo postal: {postalZip[i]}\n"
        print(mensaje)