# Importo funciones, libreries
import pygame
from candycrushutn import *
from maingame import maingame
from funciones_candycrush import *

pygame.init() # Inicio el juego
screen = pygame.display.set_mode((800,600)) # Configuro la pantalla
clock = pygame.time.Clock() 
running = True #Bucle principal
pygame.display.set_caption("Candy Crush UTN") # Titulo del juego
imagen = pygame.image.load("Candy.png") # Imagen de Candy Crush
pygame.display.set_icon(imagen) # Icono de Candy Crush (al lado del caption)
imagen = pygame.transform.scale(imagen, (100,100)) # Ajuste de tamaño d la Imagen para usarla en la pantalla principal
# Rectangulos de input, de jugar y de scoreboard
input_box = pygame.Rect(240,300,300,75)
play_box = pygame.Rect(240,400,300,75)
scoreboard_box = pygame.Rect(20,100, 200, 400)
color_activo = (232, 232, 232) # Blanco
color_inactivo = (191, 191, 191) # Gris
color_input = color_inactivo # El color default es el inactivo, pero cuando se activa pasa a blanco
active = False # Bandera para el Input
texto = "" # Texto del input
fuente = pygame.font.Font(None, 36) # Fuente
fuente_scoreboard =pygame.font.Font(None, 20) # Fuente para scoreboard
# Bucle principal
while running:
    # Array contenedor de eventos
    array_eventos = pygame.event.get()
    for event in array_eventos:
        # Si se presiona la cruz de cierre, se detiene el bucle principal
        if event.type == pygame.QUIT:
            running = False
        # En caso de que haya un click, entra a un if
        if event.type == pygame.MOUSEBUTTONDOWN:
            #En el caso de que el click sea en el rectangulo del input, lo activa
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
            # En caso de que el click sea en el rectangulo de "PLAY", usa la funcion de nuevo juego, con texto
            # y el juego principal (retorna puntos) como parametro
            if play_box.collidepoint(event.pos):
                print("Jugando al jueguito dou nashe")
                nuevo_juego(texto,maingame(screen, imagen))
        # En caso de que se aprete una tecla con el input activo, entra al if
        if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE: # Si presiona el DELETE, borra
                    texto = texto[:-1]
                elif event.key == pygame.K_RETURN: #Si presiona enter, arranca el nuevo juego
                    nuevo_juego(texto,maingame(screen, imagen)) 
                else: # Si presiona una tecla de texto, lo introduce a la cadena 
                    texto += event.unicode 
    screen.fill("green") # Fondo verde
    screen.blit(imagen, (340,20)) # Imagen Candy Crush
    color_input = color_activo if active else color_inactivo # El color de input, es el activo si la flag esta activa, de lo contrario es el inactivo
    # Rectangulos, dibujados en la pantalla, color, y los valores de los Rect ya hechos en variables
    pygame.draw.rect(screen, color_input, input_box) 
    pygame.draw.rect(screen, "purple", play_box)
    pygame.draw.rect(screen, "grey", scoreboard_box)
    scoreboard_texto = fuente.render("SCOREBOARD", True, "red") # Titulo de Scoreboard
    play_texto = fuente.render("PLAY",True, "green") # Texto de boton PLAY
    texto_renderizado = fuente.render(texto, True, (0, 0, 0)) # Texto de input
    # Bliteo en pantalla de los textos mencionados
    screen.blit(texto_renderizado, (input_box.x + 10, input_box.y + 20)) 
    screen.blit(play_texto, (play_box.x+120, play_box.y+25))
    screen.blit(scoreboard_texto, (scoreboard_box.x+15, scoreboard_box.y))
    # Espacio de SCOREBOARD hasta los integrantes del mismo
    espacio = 30
    lista_scoreboard = obtener_scoreboard() #Scoreboard
    # Recorrido de array con FOR
    for persona in lista_scoreboard:
        cadena_separada = persona.split(",") # Separo cada linea del array, con la "," devuelve ["nombre", "puntos"]
        if len(cadena_separada[0])>17: # En caso de ser muy largo el nombre, lo acorta y le pone puntos suspensivos
            cadena_separada[0] = cadena_separada[0][:17] + "..."
        screen.blit(
            fuente_scoreboard.render(f"{cadena_separada[0]}", True, "green"),
            (scoreboard_box.x, scoreboard_box.y+espacio)
        ) # Bliteo el nombre 
        screen.blit(
            fuente_scoreboard.render(f"{cadena_separada[1][:-1]}", True, "green"),
            (scoreboard_box.x+150, scoreboard_box.y+espacio)
        ) # Bliteo el puntaje
        # Sumo 20 de espacio para que no se junten todos
        espacio += 20
    pygame.display.flip()
    clock.tick(30)

pygame.quit()