from listas_personas import address, telefonos, region, country, edades, mails, nombres, postalZip
def menu():
    seguir = "si"
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
                mensaje += f"Telefono: {telefonos[i]}\n"
                mensaje += f"Pais: {country[i]}\n"
                print(mensaje)
    def datos_jovenes(edad):
        menores = []
        posicion = []
        for i in range(len(edad)):
            print(menores)
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
    def datos_mayores(edad):
        mayores = []
        posicion = []
        for i in range(len(edad)):
            if i == 0 or edad[i] > mayores[0]:
                mayores = [edad[i]]
                posicion = [i]
            elif edad[i] == mayores[0]:
                mayores.append(edad[i])
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
    while seguir == "si":
        print("""
    Menu de opciones:
    1:Importar listas
    2:Listar los datos de los usuarios de México
    3:Listar los nombre, mail y teléfono de los usuarios de Brasil
    4:Listar los datos del/los usuario/s más joven/es
    5:Obtener un promedio de edad de los usuarios
    6:De los usuarios de Brasil, listar los datos del usuario de mayor edad
    7:Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
    8:-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
    9: Cerrar menu
    """)
        opcion = int(input("Elija su opcion: "))
        match opcion:
            case 1:
                importar()
                print("Listas importadas!")
            case 2:
                datos_mexico(pais[0])
            case 3:
                datos_brasil(pais[0])
            case 4:
                datos_jovenes(edad[0])
            case 5:
                promedio_edad(edad[0])
            case 6:
                datos_mayores(edad[0])
            
menu()