import pygame
import config

class Player():
    def __init__(self, start):
        self.r = 20
        self.cords = start
        self.delta = 1
        self.rect = pygame.Rect(self.cords[0] - self.r, self.cords[1] - self.r, 2 * self.r, 2 * self.r)
    
    def render(self, screen):
        self.rect = pygame.Rect(self.cords[0] - self.r, self.cords[1] - self.r, 2 * self.r, 2 * self.r)
        pygame.draw.rect(screen, pygame.Color("black"), self.rect)

    
    def move(self, key, matrix):
        check = self.chek_wall(matrix)
        if (key == 26) and (check[0]) and (check[1]):
            self.cords = (self.cords[0], self.cords[1] - self.delta)

        if (key == 4) and (check[0]) and (check[2]):
            self.cords = (self.cords[0] - self.delta, self.cords[1])

        if (key == 22) and (check[2]) and (check[3]):
           self.cords = (self.cords[0], self.cords[1] + self.delta)

        if (key == 7) and (check[1]) and (check[3]):
            self.cords = (self.cords[0] + self.delta, self.cords[1])
    
    def chek_wall(self, matrix):
        x1 = (self.cords[0] - config.indent - self.r - 1) // config.CELL_SIZE
        y1 = (self.cords[1] - config.indent - self.r - 1) // config.CELL_SIZE
        x2 = (self.cords[0] - config.indent + self.r + 1) // config.CELL_SIZE
        y2 = (self.cords[1] - config.indent + self.r + 1) // config.CELL_SIZE
        print(x1, x2, y1, y2)
        cells = (matrix[y1][x1], matrix[y1][x2], matrix[y2][x1], matrix[y2][x2])
        return list(map(lambda cell: cell != "X", cells))
        
        