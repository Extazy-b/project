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

    while True:
        level_n, id_n = start_render(screen, fps, clock)
        while level_n != 0:
            level_n = level_render(level_n, id_n, screen, fps, clock)
    