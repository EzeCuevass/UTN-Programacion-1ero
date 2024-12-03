import pygame
from candycrushutn import *
from funciones_candycrush import *
def maingame(screen, imagen):
    puntos = 0
    caramelo_rojo  = pygame.image.load("caramelo_rojo.png")
    caramelo_rojo = pygame.transform.scale(caramelo_rojo,(100,100))
    caramelo_azul  = pygame.image.load("caramelo_azul.png")
    caramelo_azul = pygame.transform.scale(caramelo_azul,(100,100))
    caramelo_verde  = pygame.image.load("caramelo_verde.png")
    caramelo_verde = pygame.transform.scale(caramelo_verde,(100,100))
    fuente = pygame.font.Font(None, 36)
    box_caramelos = pygame.Rect(50,150,700,400)
    segundos = 11
    fin_tiempo = False
    timer = pygame.USEREVENT
    pygame.time.set_timer(timer, 1000)
    lista = [
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]},
        {"piezas":[]}
    ]
    mostrar_lista(lista)
    while not (fin_tiempo):
        array_eventos = pygame.event.get()
        for event in array_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordenada_x = int(round(event.pos[0] / 100,0)-1)
                coordenada_y = int(round((event.pos[1]-100) / 100,0)-1)
                if box_caramelos.collidepoint(event.pos):
                    intento_juego = verificar_eleccion(lista, coordenada_y, coordenada_x)
                    if intento_juego == 10:
                        lista = [
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]}
                        ]
                        mostrar_lista(lista)
                        puntos += 10
                        pygame.display.flip()
                    elif intento_juego == -1:
                        lista = [
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]}
                        ]
                        mostrar_lista(lista)
                        segundos = segundos -1
                        puntos += -1
                        pygame.display.flip()
                    else:
                        pass
            if event.type == pygame.USEREVENT:
                if event.type == timer:
                    if fin_tiempo == False:
                        segundos = segundos -1
                        if segundos <= 0:
                            fin_tiempo = True
                            return puntos

        timer_texto = fuente.render(str(segundos), True, "green")
        screen.fill("purple")
        screen.blit(imagen, (340,20))
        screen.blit(timer_texto, (100,20))
        pygame.draw.rect(screen, (74, 74, 74),box_caramelos) #LEFT, TOP, WIDTH, HEIGHT
        imprimir_carmelos(lista,screen, caramelo_rojo,caramelo_azul,caramelo_verde)
        pygame.display.flip()


def imprimir_carmelos(lista,screen, caramelo_rojo,caramelo_azul,caramelo_verde):
    coordenadas_fila = 150
    for objeto in lista:
        coordenadas_columna = 50
        for caramelo in objeto["piezas"]:
            if caramelo == 1:
                screen.blit(caramelo_rojo,(coordenadas_columna, coordenadas_fila))
            elif caramelo == 2:
                screen.blit(caramelo_azul,(coordenadas_columna, coordenadas_fila))
            elif caramelo == 3:
                screen.blit(caramelo_verde,(coordenadas_columna, coordenadas_fila))
            coordenadas_columna+=100
            if coordenadas_columna >= 700:
                coordenadas_columna = 100
        if coordenadas_fila >= 400:
            coordenadas_fila = 150
        coordenadas_fila+=100