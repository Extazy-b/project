import pygame
import config


class Block():
    def __init__(self):
        self.color = (0, 0, 0)
    
    def render(self, screen, row, column):
        rect = pygame.Rect(config.CELL_SIZE * column + config.indent, config.CELL_SIZE * row + config.indent, 
                                   config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, (255, 255, 255), rect, 1)


class Wall(Block):
    def __init__(self):
        super().__init__()
        self.color = pygame.Color("Black")
        self.moved = False


class Water(Block):
    def __init__(self):
        super().__init__()
        self.color = pygame.Color("Blue")


class Float(Block):
    def __init__(self):
        super().__init__()
        self.color = pygame.Color("Grey")


class Space(Block):
    def __init__(self):
        super().__init__()
        self.color = pygame.Color("Black")
