import pygame
from functions import create_button, move_to_button_check, active_button_mark
from database import new_account


def form_render(screen, fps, clock):
    background = pygame.image.load("image/background.jpg")
    width = 1
    
    name = ""
    font = pygame.font.Font("font.ttf", 30)

    figures = {
            "": (103, 206, 394, 188),
            "New account": (158, 231, 285, 39)
    }

    buttons = {
            "Create": (338, 338, 123, 37),
            "Cancle": (126, 338, 123, 37),
            "Write zone": (157, 280, 285, 39)
    }

    active_button = ""
    running = True

    while running:
        screen.blit(background, (0, 0))

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
                    if active_button == "Cancle":
                        running = False
                    if active_button == "Create":
                        if len(name) > 0:
                            new_account(name)
                            running = False
                width = 3 if active_button == "Write zone" else 1

            if event.type == pygame.KEYDOWN:
                if width == 3:
                    if len(name) < 17:
                        name += event.unicode
                    if event.key == 8:
                        name = name[:-1]
        
        

        for title in figures:
            create_button(screen, figures[title], title, 60, "stone_texture")
        
        if not (active_button in ("", "Write zone")):
            active_button_mark(screen, buttons[active_button])

        for title in buttons:
            create_button(screen, buttons[title], title, 30, "lava_texture")
        
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(157, 280, 285, 39), width)

        p_name = font.render(name, True, (179, 179, 179))
        screen.blit(p_name, ((157 + (285 - p_name.get_width()) // 2), 
                    (280 + (39 - p_name.get_height()) // 2)))

        pygame.display.flip()
    
    screen.blit(background, (0, 0))