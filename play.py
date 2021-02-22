import pygame
from level import Level
from player import Player
from enemy import Enemy
from levels import test
from functions import start_cords_generstion, get_enemy_info



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('test')

    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)

    board = Level(1)
    player = Player(start_cords_generstion(board.matrix))
    enemy = Enemy(get_enemy_info(board.matrix))

    fps = 100
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        keys = list(pygame.key.get_pressed())
        if 1 in keys:
            player.move(keys.index(1), test)

        screen.blit(board.image, (50, 50))
        #board.render(screen)
        player.render(screen)
        enemy.render(screen)
        pygame.display.flip()
        clock.tick(fps)