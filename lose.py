import pygame
from functions import create_button, move_to_button_check, active_button_mark


def lose_render(screen, fps, clock, level_n):
    background = pygame.image.load("image/background.jpg")
    figures = {
            "": (184, 238, 233, 124),
            "You lose": (206, 251, 189, 24)
    }

    buttons = {
            "Main": (195, 322, 77, 20),
            "Again": (330, 322, 77, 20)
    }

    active_button = ""
    running = True  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
                        
            if event.type == pygame.MOUSEMOTION:
                active_button = move_to_button_check(screen, event.pos, buttons)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_button != "": 
                    running = False
                    if active_button == "Again":
                        result = level_n
                    if active_button == "Main":
                        screen.blit(background, (0, 0))
                        result = 0
       
        for title in figures:
            create_button(screen, figures[title], title, 60, "stone_texture")
        
        if active_button != "":
            active_button_mark(screen, buttons[active_button])

        for title in buttons:
            create_button(screen, buttons[title], title, 20, "lava_texture")
        

        pygame.display.flip()
    return result