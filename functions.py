import os
import sys
import pygame
import json
import config


def start_cords_generstion(matrix):
    for i in range(config.N):
        if "S" in matrix[i]:
            y = i
            x = matrix[i].index("S")
            cords = (config.indent + ((y + 1) * (config.CELL_SIZE)), config.indent + ((x + 1) * (config.CELL_SIZE)))
            return cords


def get_matrix(level_n):
    with open("levels.json", "r") as levels:
        levels = json.load(levels)
        return levels[level_n]


def get_enemy(level_n):
    with open("enemy.json", "r") as enemys:
        enemys = json.load(enemys)
        return enemys[level_n]


def create_button(screen, data, text, size, background):
    x, y, width, height = data
    background = pygame.image.load(f"image/{background}.jpg")
    background = pygame.transform.scale(background, (width, height))

    font = pygame.font.Font("font.ttf", size)
    title = font.render(text, True, (179, 179, 179))

    if text != "Write zone":
        screen.blit(background, (x, y))
        screen.blit(title, ((x + (width - title.get_width()) // 2), 
                    (y + (height - title.get_height()) // 2)))


def move_to_button_check(screen, mouse_pos, button_info):
    mouse_x, mouse_y = mouse_pos
    for title in button_info:
        x, y, width, height = button_info[title]
        if mouse_x in range(x, x + width) and mouse_y in range(y, y + height):
            if not (title in ("Dungeon time", "",)):
                rect = pygame.Rect(x - 4, y - 4, width + 8, height + 8)
                if title != "Write zone":
                    pygame.draw.rect(screen, pygame.Color("Red"), rect)
                return title
    return ""
    

def active_button_mark(screen, button_pos):
    x, y, width, height = button_pos
    rect = pygame.Rect(x - 4, y - 4, width + 8, height + 8)
    pygame.draw.rect(screen, pygame.Color("Red"), rect)


def create_rating_elem(screen, rating):
    x = 338
    y = 156
    width = 229
    height = 32
    for elem in range(8):
        rect = pygame.Rect(x, (y + (elem * height)), width, height)
        pygame.draw.rect(screen, (255, 255, 255), rect, 1)
        if not (rating[elem][0] is None):
            font = pygame.font.Font("font.ttf", 30)
            title = font.render(f"{rating[elem][0][:10]}: {rating[elem][1]}", True, (0, 179, 0))

            screen.blit(title, ((x + (width - title.get_width()) // 2), 
                        (y + (elem * height) + (height - title.get_height()) // 2)))
        
    
def show_account(screen, name, score, last_level):
    background = pygame.image.load("image/stone_texture.jpg")
    background = pygame.transform.scale(background, (248, 142))
    
    font = pygame.font.Font("font.ttf", 30)

    title = font.render(name, True, (0, 179, 0))
    level = font.render(f"Level: {last_level}", True, (0, 179, 0))

    logo = pygame.image.load("image/hero.png")

    screen.blit(background, (34, 158))
    screen.blit(logo, (56, 233))

    screen.blit(title, ((56 + (206 - title.get_width()) // 2), 
                (176 + (31 - title.get_height()) // 2)))

    screen.blit(level, ((114 + (147 - level.get_width()) // 2), 
                (223 + (39 - level.get_height()) // 2)))

