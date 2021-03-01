import pygame
from functions import create_button, move_to_button_check, active_button_mark, create_rating_elem, show_account
from database import get_rating
from new_account import form_render


def start_render(screen, fps, clock):
    running = True
    is_show_account = False
    background = pygame.image.load("image/background.jpg")
    last_level = -1

    active_button = ""
    buttons = {"Dungeon time": (34, 28, 532, 86),
               "Exit": (388, 455, 178, 78),
               "Play": (34, 455, 249, 78),
               "New": (34, 330, 248, 81),
               "": (338, 156, 228, 256)}
    while running:
        rating = get_rating()
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEMOTION:
                active_button = move_to_button_check(screen, event.pos, buttons)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_button != "": 
                    if active_button == "Exit":
                        exit()
                    if active_button == "Play":
                        if last_level != -1:
                            running = False
                    if active_button == "New":
                        form_render(screen, fps, clock)
                elif (event.pos[0] in range(338, 567)) and (event.pos[1] in range(156, 412)):
                    x = (event.pos[1] - 156) // 32
                    if rating[x][0] != None:
                        is_show_account = True
        if is_show_account:
            last_level = rating[x][2].index(0) if 0 in rating[x][2] else 8
            last_level = 1 if last_level == 0 else last_level
            show_account(screen, rating[x][0], rating[x][1], last_level)

        if active_button != "":
            active_button_mark(screen, buttons[active_button])

        for title in buttons:
            create_button(screen, buttons[title], title, 80, "stone_texture")
        
        create_rating_elem(screen, rating)

        pygame.display.flip()
    screen.blit(background, (0, 0))

    return last_level, x