# Importaciones de libreria y funciones
import pygame
from candycrushutn import *
from funciones_candycrush import *
# Funcion
def maingame(screen, imagen):
    puntos = 0 # Incializacion de puntos
    # Seteo de caramelos
    caramelo_rojo  = pygame.image.load("caramelo_rojo.png")
    caramelo_rojo = pygame.transform.scale(caramelo_rojo,(100,100))
    caramelo_azul  = pygame.image.load("caramelo_azul.png")
    caramelo_azul = pygame.transform.scale(caramelo_azul,(100,100))
    caramelo_verde  = pygame.image.load("caramelo_verde.png")
    caramelo_verde = pygame.transform.scale(caramelo_verde,(100,100))
    fuente = pygame.font.Font(None, 36) # Fuente para contador
    box_caramelos = pygame.Rect(50,150,700,400) # Rect en el que estan los caramelos
    segundos = 11 # Tiempo
    fin_tiempo = False # Bandera
    timer = pygame.USEREVENT 
    pygame.time.set_timer(timer, 1000) # Cada 1000 milisegundos, usa el userevent de timer
    # Incializacion de lista
    lista = [
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]}
    ]
    mostrar_lista(lista)
    # Bucle principal, mientras NO se termine el tiempo, ejecuta lo que esta adentro
    while not (fin_tiempo):
        # Array de eventos
        array_eventos = pygame.event.get()
        for event in array_eventos: # Por cada evento en el array:
            if event.type == pygame.QUIT: # Si es quit cierra el juego
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Si se presiona el boton del mouse:
                # Agarro la coordennada x, y la coordenada y para usarlas en la funcion de CC consola
                coordenada_x = int(round(event.pos[0] / 100,0)-1)
                coordenada_y = int(round((event.pos[1]-100) / 100,0)-1)
                if box_caramelos.collidepoint(event.pos): # Si el click esta adentro de la caja que contiene los caramelos: 
                    intento_juego = verificar_eleccion(lista, coordenada_y, coordenada_x) # Verifico la eleccion con las coordenadas
                    if intento_juego == 10: # En caso de ser 10:
                        lista = [
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]}
                        ] # Reseteo la lista
                        mostrar_lista(lista)
                        puntos += 10 # Sumo puntos
                        pygame.display.flip() # Actualizo
                    elif intento_juego == -1: # En caso de ser -1 (error)
                        lista = [
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]}
                        ] # Reseteo la lista
                        mostrar_lista(lista)
                        segundos = segundos -1 # Resto un segundo
                        puntos += -1 # Resto un punto
                        pygame.display.flip() # Actualizo
            if event.type == pygame.USEREVENT: # Si hay un userevent
                if event.type == timer: # Si ese user event corresponde al timer
                    if fin_tiempo == False: # En caso que no se haya llegado al fin del tiempo, se resta 1 segundo
                        segundos = segundos -1
                        if segundos <= 0: # Si segundos es menor o igual a 0
                            fin_tiempo = True # Bajo la bandera, rompe el bucle
                            return puntos # Retorna puntos
                        
        timer_texto = fuente.render(str(segundos), True, "green") # Texto de timer
        screen.fill("purple") # Fondo violeta
        screen.blit(imagen, (340,20)) # Imagen candy crush
        screen.blit(timer_texto, (100,20)) # Bliteo del texto del timer
        pygame.draw.rect(screen, (74, 74, 74),box_caramelos) # Dibuja la caja de los caramelos en la pantalla
        imprimir_carmelos(lista,screen, caramelo_rojo,caramelo_azul,caramelo_verde) # Utilizo la funcion de imprimir caramelos
        pygame.display.flip() # Actualizo


def imprimir_carmelos(lista,screen, caramelo_rojo,caramelo_azul,caramelo_verde): # Funcion para imprimir caramelos
    coordenadas_fila = 150 # Donde va a estar la primera fila
    for objeto in lista: # Por cada diccionario en la lista:
        coordenadas_columna = 50 # Donde va a estar la primera columna
        for caramelo in objeto["piezas"]: # Por cada caramelo en el diccionario:
            # Dependiendo del valor (1,2,3), blitea un caramelo del color correspondiente, en las coordenadas correspondientes
            if caramelo == 1: 
                screen.blit(caramelo_rojo,(coordenadas_columna, coordenadas_fila))
            elif caramelo == 2:
                screen.blit(caramelo_azul,(coordenadas_columna, coordenadas_fila))
            elif caramelo == 3:
                screen.blit(caramelo_verde,(coordenadas_columna, coordenadas_fila))
            coordenadas_columna+=100 # Con cada caramelo, se suma 100 a la coordenada, para que no esten pegados
            if coordenadas_columna >= 700: # Cuando llega a 700, resetea
                coordenadas_columna = 100
        if coordenadas_fila >= 400: # Cuando llega a 400, resetea
            coordenadas_fila = 150
        coordenadas_fila+=100 # Con cada fila, se suma 100 a la coordenada, para que no esten pegadas