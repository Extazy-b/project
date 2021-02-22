import pygame
from level import Level
from player import Player
from levels import test



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('test')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    board = Level(1)
    player = Player((190, 190))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = list(pygame.key.get_pressed())
        if 1 in keys:
            player.move(keys.index(1), test)
        screen.fill(pygame.Color('black'))
        board.render(screen)
        player.render(screen)
        pygame.display.flip()