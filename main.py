import pygame
from level_play import level_render
from start_window import start_render

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Dungeon time')

    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)

    fps = 100
    clock = pygame.time.Clock()

    start_render(screen, fps, clock)
    level_render("1", screen, fps, clock)