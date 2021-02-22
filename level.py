import config
import levels
import pygame
import blocks

class Level():
    def __init__(self, level_n):
        self.work = True
        self.n = config.N
        self.cell_size = config.CELL_SIZE
        self.matrix = levels.test
        self.top = self.left = 50

    def render(self, screen):
        for row in range(self.n):
            for column in range(self.n):
                cell = self.matrix[row][column]
                block = config.blocks[cell]
                block.render(screen, row, column)