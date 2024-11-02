def mostrar_heroes(heroes):
    for heroe in heroes:
        print(f"Nombre: {heroe['nombre']}")
        print(f"Identidad: {heroe['identidad']}")
        print(f"Altura: {heroe['altura']}")
        print(f"Peso: {heroe['peso']}")
        print(f"Fuerza: {heroe['fuerza']}")
        print(f"Inteligencia: {heroe['inteligencia']}")
        print("\n")

def ordenar_por_nombre(heroes):
    """
    Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por
    Nombre de manera ascendente.
    """
    for i in range(len(heroes)):
        for j in range(i,len(heroes)):
            if heroes[i]["nombre"] > heroes[j]["nombre"]:
                aux = heroes[j]
                heroes[j] = heroes[i]
                heroes[i] = aux
    mostrar_heroes(heroes)
def superheroe_mas_debil(heroes):
    """
    Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de
    género M.
    """
    min = 0
    bandera = True
    debiles = []
    posicion = 0
    for i in range(len(heroes)):
        if heroes[i]["fuerza"] < min or bandera:
            bandera = False
            min = heroes[i]["fuerza"]
            posicion = i
        if heroes[i]["fuerza"] <= 15:
            debiles.append(heroes[i])
    print("Los superheroes mas debiles son: ")
    mostrar_heroes(debiles)
    print(f"El superheroe mas debil es: {heroes[posicion]['nombre']}")
def separar_inteligencia(heroes):
    """
    Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
    """
    high = []
    average = []
    good = []
    for heroe in heroes:
        if heroe['inteligencia'] == "high":
            high.append(heroe)
        elif heroe['inteligencia'] == "average":
            average.append(heroe)
        elif heroe['inteligencia'] == "good":
            good.append(heroe)
        else:
            print(f"No se tienen datos sobre la inteligencia de {heroe['nombre']}")
    print("Heroes de inteligencia alta: ")
    mostrar_heroes(high)
    print("Heroes de inteligencia promedio: ")
    mostrar_heroes(average)
    print("Heroes de inteligencia buena: ")
    mostrar_heroes(good)
def calcular_imc(heroes):
    """
    Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un
    nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el
    IMC calculado.
    """
    for heroe in heroes:
        imc = heroe["peso"] / ((heroe["altura"]/100)**2)
        heroe["imc"] = imc

    for heroe in heroes:
        print(f"Nombre: {heroe['nombre']}")
        print(f"Identidad: {heroe['identidad']}")
        print(f"Altura: {heroe['altura']}")
        print(f"Peso: {heroe['peso']}")
        print(f"Fuerza: {heroe['fuerza']}")
        print(f"Inteligencia: {heroe['inteligencia']}")
        print(f"IMC: {heroe['imc']}")
        print("\n")