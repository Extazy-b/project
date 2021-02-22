import pygame
import config


class Enemy():
    def __init__(self, start):
        self.r = 12
        self.cords = start
        self.delta = 1
        self.rect = pygame.Rect(self.cords[0] - self.r, self.cords[1] - self.r, 2 * self.r, 2 * self.r)
    
    def render(self, screen):
        self.rect = pygame.Rect(self.cords[0] - self.r, self.cords[1] - self.r, 2 * self.r, 2 * self.r)
        pygame.draw.rect(screen, pygame.Color("black"), self.rect)
    
"""     def move(self, orient):
        if orient == "hor": """
