import pygame
import config

class Player():
    def __init__(self, start):
        self.r = 20
        self.cords = start
        self.delta = 2
        self.rect = pygame.Rect(self.cords[0] - self.r, self.cords[1] - self.r, 2 * self.r, 2 * self.r)
        self.image = pygame.image.load("image\hero.png")
        self.image = self.image.convert_alpha()
        self.side = "right"
    
    def render(self, screen):
        self.rect = pygame.Rect(self.cords[0] - self.r, self.cords[1] - self.r, 2 * self.r, 2 * self.r)
        pygame.draw.rect(screen, pygame.Color("black"), self.rect)
        screen.blit(self.image, (self.cords[0] - self.r, self.cords[1] - self.r))

    
    def move(self, key, matrix):
        if (key == 26): #w
            y = (self.cords[1] - config.indent - self.r - self.delta) // config.CELL_SIZE
            x1 = (self.cords[0] - config.indent - self.r) // config.CELL_SIZE
            x2 = (self.cords[0] - config.indent + self.r) // config.CELL_SIZE
            if not ("X" in matrix[y][x1: x2 + 1]):
                self.delta = 1 if "_" in matrix[y][x1: x2 + self.delta] else 2
                self.cords = (self.cords[0], self.cords[1] - self.delta)

        if (key == 4): #a
            if self.side == "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.side = "left"
            flag = True
            water = False
            x = (self.cords[0] - config.indent - self.r - self.delta) // config.CELL_SIZE
            y1 = (self.cords[1] - config.indent - self.r) // config.CELL_SIZE
            y2 = (self.cords[1] - config.indent + self.r) // config.CELL_SIZE
            for i in range(y1, y2 + 1):
                if "X" in matrix[i][x]:
                    flag = False
                if "_" in matrix[i][x]:
                    water = True
            if flag:
                self.delta = 1 if water else 2
                self.cords = (self.cords[0] - self.delta, self.cords[1]) 

        if (key == 22): #s
            y = (self.cords[1] - config.indent + self.r + self.delta) // config.CELL_SIZE
            x1 = (self.cords[0] - config.indent - self.r) // config.CELL_SIZE
            x2 = (self.cords[0] - config.indent + self.r) // config.CELL_SIZE
            if not ("X" in matrix[y][x1: x2 + 1]):
                self.delta = 1 if "_" in matrix[y][x1: x2 + 1] else 2
                self.cords = (self.cords[0], self.cords[1] + self.delta)

        if (key == 7): #d
            if self.side == "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.side = "right"
            flag = True
            water = False
            x = (self.cords[0] - config.indent + self.r + self.delta) // config.CELL_SIZE
            y1 = (self.cords[1] - config.indent - self.r) // config.CELL_SIZE
            y2 = (self.cords[1] - config.indent + self.r) // config.CELL_SIZE
            for i in range(y1, y2 + 1):
                if "X" in matrix[i][x]:
                    flag = False
                if "_" in matrix[i][x]:
                    water = True
            if flag:
                self.delta = 1 if water else 2
                self.cords = (self.cords[0] + self.delta, self.cords[1]) 
   
    def chek_wall(self, matrix):
        x1 = (self.cords[0] - config.indent - self.r - self.delta) // config.CELL_SIZE
        y1 = (self.cords[1] - config.indent - self.r - self.delta) // config.CELL_SIZE


        print(x1, x2, y1, y2)
        cells = (matrix[y1][x1], matrix[y1][x2], matrix[y2][x1], matrix[y2][x2])
        return list(map(lambda cell: cell != "X", cells))
        
        