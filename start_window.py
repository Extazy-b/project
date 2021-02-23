import pygame
from functions import create_button, move_to_button_check, active_button_mark


def start_render(screen, fps, clock):
    running = True
    background = pygame.image.load("image/background.jpg")
    active_button = ""
    buttons = {"Dungeon time": (34, 28, 532, 86),
               "Exit": (388, 455, 178, 78),
               "Play": (34, 455, 249, 78),
               "":(338, 156, 228, 256) }
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

            if event.type == pygame.MOUSEMOTION:
                active_button = move_to_button_check(screen, event.pos, buttons)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_button != "": 
                    if active_button == "Exit":
                        exit()
                    if active_button == "Play":
                        running = False
        if active_button != "":
            active_button_mark(screen, buttons[active_button])

        for title in buttons:
            create_button(screen, buttons[title], title, 80, "stone_texture")

        pygame.display.flip()
    screen.blit(background, (0, 0))