import pygame
from level import Level
from player import Player
from enemy import Enemy
from pause_menu import menu_render
from functions import start_cords_generstion, get_enemy_info, get_matrix


def level_render(level_n, screen, fps, clock):    
    board = Level(level_n)
    matrix = get_matrix(level_n)
    player = Player(start_cords_generstion(board.matrix))
    enemy = Enemy(get_enemy_info(board.matrix))

    background = pygame.image.load("image/background.jpg")
    shadow = pygame.image.load("image/shadow.png")

    pause = False
    running = True

    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    pause = True
    
        keys = list(pygame.key.get_pressed())
        if 1 in keys:
            player.move(keys.index(1), matrix)

        screen.blit(board.image, (50, 50))
        #board.render(screen)
        player.render(screen)
        enemy.render(screen)
        if pause:
            screen.blit(shadow, (0, 0))
            menu_render(screen, fps, clock)
            pause = False
        pygame.display.flip()
        clock.tick(fps)