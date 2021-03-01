import pygame
from functions import create_button, move_to_button_check, active_button_mark


def win_render(screen, fps, clock, level_n, score):
    figures = {
            "": (184, 238, 233, 124),
            "You won": (206, 251, 189, 24)
    }

    buttons = {
            "Continue": (195, 322, 77, 20),
            "Again": (330, 322, 77, 20)
    }

    active_button = ""
    running = True

    star_img = pygame.image.load("image/star.jpg")
    star_empty_img = pygame.image.load("image/star_empty.jpg")

    star_img.set_colorkey((255, 255, 255))
    star_empty_img.set_colorkey((255, 255, 255))    

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
                    if active_button == "Continue":
                        result = level_n + 1 
       
        for title in figures:
            create_button(screen, figures[title], title, 60, "stone_texture")
        
        if active_button != "":
            active_button_mark(screen, buttons[active_button])

        for title in buttons:
            create_button(screen, buttons[title], title, 20, "lava_texture")
        
        for star in range(3):
            screen.blit(star_empty_img, (234 + (53 * star), 288))
        
        for star in range(score):
            screen.blit(star_img, (234 + (53 * star), 288))

        pygame.display.flip()
        clock.tick(fps)
    return result