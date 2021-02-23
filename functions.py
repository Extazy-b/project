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


def get_enemy_info(matrix):
    orient = ""
    for i in range(config.N):
        if "E" in matrix[i]:
            if matrix[i].count("E") == 2:
                orient = "hor"
                y = i
                x = matrix[i].index("E")
                cords = (config.indent + ((y + 1) * (config.CELL_SIZE)), 
                         config.indent + ((x + 1) * (config.CELL_SIZE))) 
                return cords           
            else:
                orient = "vert"


def get_matrix(level_n):
    with open("levels.json", "r") as levels:
        levels = json.load(levels)
        return levels[level_n]


def create_button(screen, data, text, size, background):
    x, y, width, height = data
    background = pygame.image.load(f"image/{background}.jpg")
    background = pygame.transform.scale(background, (width, height))

    font = pygame.font.Font("font.ttf", size)
    title = font.render(text, True, (179, 179, 179))

    screen.blit(background, (x, y))
    screen.blit(title, ((x + (width - title.get_width()) // 2), (y + (height - title.get_height()) // 2)))


def move_to_button_check(screen, mouse_pos, button_info):
    mouse_x, mouse_y = mouse_pos
    for title in button_info:
        x, y, width, height = button_info[title]
        if mouse_x in range(x, x + width) and mouse_y in range(y, y + height):
            if not (title in ("Dungeon time", "",)):
                rect = pygame.Rect(x - 4, y - 4, width + 8, height + 8)
                pygame.draw.rect(screen, pygame.Color("Red"), rect)
                return title
    return ""
    


def active_button_mark(screen, button_pos):
    x, y, width, height = button_pos
    rect = pygame.Rect(x - 4, y - 4, width + 8, height + 8)
    pygame.draw.rect(screen, pygame.Color("Red"), rect)
        