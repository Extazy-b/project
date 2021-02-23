import config
import levels
import pygame
import blocks
from functions import get_matrix

class Level():
    def __init__(self, level_n):
        self.work = True
        self.n = config.N
        self.cell_size = config.CELL_SIZE
        self.matrix = get_matrix(level_n)
        self.top = self.left = 50
        self.image = pygame.image.load(f"image/{level_n}.JPG")
        #self.all_sprites = pygame.sprite.Group()

    def render(self, screen):
        for row in range(self.n):
            for column in range(self.n):
                cell = self.matrix[row][column]
                block = config.blocks[cell]
                block.render(screen, row, column, self)
        #self.all_sprites.draw(screen)