import pygame
from candycrushutn import *
from maingame import maingame
pygame.init() # Inicio el juego
screen = pygame.display.set_mode((800,600)) # Configuro la pantalla
clock = pygame.time.Clock() 
running = True
pygame.display.set_caption("Candy Crush UTN") # Titulo del juego

imagen = pygame.image.load("Candy.png")
pygame.display.set_icon(imagen)
imagen = pygame.transform.scale(imagen, (100,100))
input_box = pygame.Rect(240,300,300,75) # Left, Top, Width, Heigth
play_box = pygame.Rect(240,400,300,75) # Left, Top, Width, Heigth
scoreboard_box = pygame.Rect(20,100, 200, 400)
color_activo = (232, 232, 232)
color_inactivo = (191, 191, 191)
color_input = color_inactivo
active = False
texto = ""
fuente = pygame.font.Font(None, 36)
fuente_scoreboard =pygame.font.Font(None, 20)

while running:
    array_eventos = pygame.event.get()
    for event in array_eventos:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                print("Click en el input")
                active = True
            else:
                print("Ckick Afuera del input")
                active = False
            if play_box.collidepoint(event.pos):
                print("Jugando al jueguito dou nashe")
                nuevo_juego(texto,maingame(screen, imagen))
        if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif event.key == pygame.K_RETURN:
                    nuevo_juego(texto,maingame(screen, imagen))
                else:
                    texto += event.unicode
    screen.fill("green")
    screen.blit(imagen, (340,20))
    color_input = color_activo if active else color_inactivo
    pygame.draw.rect(screen, color_input, input_box)
    pygame.draw.rect(screen, "purple", play_box)
    pygame.draw.rect(screen, "grey", scoreboard_box)
    scoreboard_texto = fuente.render("SCOREBOARD", True, "red")
    play_texto = fuente.render("PLAY",True, "green")
    texto_renderizado = fuente.render(texto, True, (0, 0, 0))
    screen.blit(texto_renderizado, (input_box.x + 10, input_box.y + 20))
    screen.blit(play_texto, (play_box.x+120, play_box.y+25))
    screen.blit(scoreboard_texto, (scoreboard_box.x+15, scoreboard_box.y))
    espacio = 30
    lista_scoreboard = obtener_scoreboard()
    for persona in lista_scoreboard:
        cadena_separada = persona.split(",")
        if len(cadena_separada[0])>17:
            cadena_separada[0] = cadena_separada[0][:17] + "..."
        screen.blit(
            fuente_scoreboard.render(f"{cadena_separada[0]}", True, "green"),
            (scoreboard_box.x, scoreboard_box.y+espacio)
        )
        screen.blit(
            fuente_scoreboard.render(f"{cadena_separada[1][:-1]}", True, "green"),
            (scoreboard_box.x+150, scoreboard_box.y+espacio)
        )
        
        espacio += 20
    pygame.display.flip()
    clock.tick(30)

pygame.quit()