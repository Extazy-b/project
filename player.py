import pygame
import config

class Player():
    def __init__(self, start):
        self.r = 20
        self.cords = start
        self.delta = 2
        self.orient = [0, 1]
        self.rect = pygame.Rect(self.cords[0] - self.r, self.cords[1] - self.r, 2 * self.r, 2 * self.r)

        self.image = pygame.image.load("image\hero.png")
        self.heart_image = pygame.image.load("image\heart.jpg")

        self.image.set_colorkey((0, 255, 0))
        self.score = 0

        self.side = "right"
        self.heart = 8
    
    def render(self, screen):
        rect = pygame.Rect(config.indent, config.indent, ((self.heart - 1) * 33), 24)
        pygame.draw.rect(screen, (0, 0, 255), rect)
        for elem in range(self.heart):
            screen.blit(self.heart_image, (elem * 33 + config.indent, config.indent))
        screen.blit(self.image, (self.cords[0] - self.r, self.cords[1] - self.r))

    def move(self, key, matrix):
        if (key == 26): #w
            y = (self.cords[1] - config.indent - self.r - self.delta) // config.CELL_SIZE
            x1 = (self.cords[0] - config.indent - self.r) // config.CELL_SIZE
            x2 = (self.cords[0] - config.indent + self.r) // config.CELL_SIZE
            if not ("X" in matrix[y][x1: x2 + 1]):
                self.delta = 1 if "_" in matrix[y][x1: x2 + self.delta] else 2
                self.cords = (self.cords[0], self.cords[1] - self.delta)
                self.orient = [1, -1]

        if (key == 4): #a
            if self.side == "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.image.set_colorkey((0, 255, 0))
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
                self.orient = [0, -1] 

        if (key == 22): #s
            y = (self.cords[1] - config.indent + self.r + self.delta) // config.CELL_SIZE
            x1 = (self.cords[0] - config.indent - self.r) // config.CELL_SIZE
            x2 = (self.cords[0] - config.indent + self.r) // config.CELL_SIZE
            if not ("X" in matrix[y][x1: x2 + 1]):
                self.delta = 1 if "_" in matrix[y][x1: x2 + 1] else 2
                self.cords = (self.cords[0], self.cords[1] + self.delta)
                self.orient = [1, 1]

        if (key == 7): #d
            if self.side == "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.image.set_colorkey((0, 255, 0))
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
                self.orient = [0, 1]
    
    def isfinish(self, screen, finish):
        x = finish[0] * config.CELL_SIZE + config.indent
        y = finish[1] * config.CELL_SIZE + config.indent

        return ((self.cords[0] in range(x, x + config.CELL_SIZE * 2)) and 
                (self.cords[1] in range(y, y + config.CELL_SIZE)))
    
    
    def attak(self, screen, enemy_pos):
        rull_1 = enemy_pos[self.orient[0]] in range(self.cords[self.orient[0]],
                                                self.cords[self.orient[0]] + (self.orient[1] * 30), 
                                                self.orient[1])
        rull_2 = enemy_pos[1 - self.orient[0]] in range(self.cords[1 - self.orient[0]] - self.r,
                                                    self.cords[1 - self.orient[0]] + self.r)

        if (rull_1 and rull_2):
            self.score += 10
            return True