from Package_Input import Input
from Package_Lists import Lists

def cargar_paciente(pacientes):
        """
        Funcion para imprimir pacientes.
        """
        cargar_mas = "si"
        while cargar_mas == "si":
            num_historia = Input.get_int("Ingrese el numero de historia del paciente: ", min=0)
            nombre = Input.get_string("Ingrese el nombre del paciente: ")
            edad = Input.get_int("Ingrese la edad del paciente: ", min=0)
            diagnostico = Input.get_string("Ingrese el diagnostico del paciente: ")
            dias_internado = Input.get_int("Ingrese los dias que lleva internado el paciente: ", min=0)
            paciente_nuevo = [num_historia,nombre,edad,diagnostico,dias_internado]
            pacientes.append(paciente_nuevo)
            print("Paciente cargado!")
            cargar_mas = Input.get_string("Desea cargar mas pacientes? si/no: ").lower()
    
def mostrar_pacientes(pacientes):
    """
    Funcion para imprimir cada paciente de la lista.
    """
    for paciente in pacientes:
        print(f"Paciente: {paciente[1]}; Edad: {paciente[2]}; Diagnostico: {paciente[3]}; Dias internado: {paciente[4]}; Numero de historia clinica: {paciente[0]}")

def buscar_historia_clinica(pacientes,numero_historia):
    """
    Funcion para buscar paciente por numero de historia clinica.
    """
    bandera = False
    for paciente in pacientes:
        if paciente[0] == numero_historia:
            bandera = True
            print(f"Paciente: {paciente[1]}; Edad: {paciente[2]}; Diagnostico: {paciente[3]}; Dias internado: {paciente[4]}; Numero de historia clinica: {paciente[0]}")
    if bandera == False:
        print("No se encontro ningun paciente con ese numero de historia clinica.")
    
def ordenar_pacientes(pacientes):
    """
    Funcion para ordenar pacientes por numero de historia clinica.
    """
    for i in range(len(pacientes)):
        for j in range(i+1,len(pacientes)):
            if pacientes[i][0] > pacientes[j][0]:
                Lists.swapear(pacientes,i,j)
    mostrar_pacientes(pacientes)
    print("Pacientes ordenados!")
def mas_dias_internado(pacientes):
    """
    Funcion que imprime el paciente con mas dias internado
    """
    maximo = 0
    primer_ingreso = True
    posicion = 0
    for i in range(len(pacientes)):
        if primer_ingreso == True or pacientes[i][4] > maximo: 
            primer_ingreso = False
            maximo = pacientes[i][4]
            posicion = i
    print(f"El paciente con mas dias internado es {pacientes[posicion][1]}, con {pacientes[posicion][4]} dias internado.")
    
def menos_dias_internado(pacientes):
    """
    Funcion que imprime el paciente con menos dias internado
    """
    minimo = 0
    primer_ingreso = True
    posicion = 0
    for i in range(len(pacientes)):
        if primer_ingreso == True or pacientes[i][4] < minimo: 
            primer_ingreso = False
            minimo = pacientes[i][4]
            posicion = i
    print(f"El paciente con mas dias internado es {pacientes[posicion][1]}, con {pacientes[posicion][4]} dias internado.")
    
def internado_5(pacientes):
    """
    Funcion que imprime los pacientes con mas de 5 dias internados
    """
    mas_de_5_dias = []
    for i in range(len(pacientes)):
            if pacientes[i][4] > 5: 
                mas_de_5_dias.append(pacientes[i])
    for paciente in mas_de_5_dias:
        print(f"Paciente: {paciente[1]}; Edad: {paciente[2]}; Diagnostico: {paciente[3]}; Dias internado: {paciente[4]}; Numero de historia clinica: {paciente[0]}")
def cantidad_pacientes_5_dias(pacientes):
    """
    Funcion que imprime la cantidad de pacientes con mas de 5 dias internado
    """
    mas_de_5_dias = 0
    for i in range(len(pacientes)):
            if pacientes[i][4] > 5: 
                mas_de_5_dias += 1
    print(f"La cantidad de pacientes con mas de 5 dias internados es de {mas_de_5_dias}.")
def promedio_internaciones(pacientes):
    """
    Funcion que promedia los dias internados que pasan los pacientes en el hospital.
    """
    total_dias_internado = 0
    for i in range(len(pacientes)):
            if pacientes[i][4] > 5: 
                total_dias_internado += pacientes[i][4]
    promedio = total_dias_internado / len(pacientes)
    print(f"El promedio de dias de internacion de los pacientes es de: {promedio}")