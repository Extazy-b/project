import os
import sys
import pygame
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