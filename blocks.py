import pygame
import config

class Block():
    def __init__(self):
        self.color = (0, 0, 0)
    
    def render(self, screen, row, column, level):
        rect = pygame.Rect(config.CELL_SIZE * column + config.indent, config.CELL_SIZE * row + config.indent, 
                                   config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, (255, 255, 255), rect, 1)

        """ sprite = pygame.sprite.Sprite(level.all_sprites)
        sprite.image = self.image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = config.CELL_SIZE * column + config.indent
        sprite.rect.y = config.CELL_SIZE * row + config.indent """

class Wall(Block):
    def __init__(self):
        super().__init__()
        self.color = pygame.Color("Black")
        self.moved = False
        #self.image = pygame.image.load("image/wall.jpg")


class Water(Block):
    def __init__(self):
        super().__init__()
        #self.color = pygame.Color("Blue")
        #self.image = pygame.image.load("image/water.jpg")


class Float(Block):
    def __init__(self):
        super().__init__()
        self.color = pygame.Color("Grey")
        #self.image = pygame.image.load("image/float.jpg")


class Space(Block):
    def __init__(self):
        super().__init__()
        self.color = pygame.Color("Black")
