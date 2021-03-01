import pygame
from os import system
from functions import create_button, move_to_button_check, active_button_mark


def menu_render(screen, fps, clock):
    figures = {
            "": (194, 113, 212, 375),
            "Pause": (223, 129, 155, 74)
    }

    buttons = {
            "Continue": (222, 238, 155, 39),
            "Management": (222, 328, 155, 39),
            "Exit": (222, 417, 155, 39)
    }

    active_button = ""
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    running = False
            
            if event.type == pygame.MOUSEMOTION:
                active_button = move_to_button_check(screen, event.pos, buttons)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_button != "": 
                    if active_button == "Exit":
                        exit()
                    if active_button == "Continue":
                        running = False 
                    if active_button == "Management":
                        system("management.py")
       
        for title in figures:
            create_button(screen, figures[title], title, 60, "stone_texture")
        
        if active_button != "":
            active_button_mark(screen, buttons[active_button])

        for title in buttons:
            create_button(screen, buttons[title], title, 30, "lava_texture")

        pygame.display.flip()