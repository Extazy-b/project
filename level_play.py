import pygame
from level import Level
from player import Player
from enemy import Enemy
from pause_menu import menu_render
from win import win_render
from lose import lose_render
from functions import start_cords_generstion, get_enemy, get_matrix
from database import update
import config


def level_render(level_n, id_n, screen, fps, clock):    
    board = Level(str(level_n))
    matrix = get_matrix(str(level_n))
    player = Player(start_cords_generstion(board.matrix))
    enemyes = get_enemy(str(level_n))
    finish = enemyes.pop(0)
    enemyes = [Enemy(enemy) for enemy in enemyes]


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
                if event.unicode == " ":
                    for enemy in enemyes:
                        if player.attak(screen, enemy.cords):
                            enemy.life = False
                if event.key == 27:
                    pause = True

        keys = list(pygame.key.get_pressed())
        if 1 in keys:
            player.move(keys.index(1), matrix)

        screen.blit(board.image, (50, 50))
        #board.render(screen)
        player.render(screen)

        for enemy in enemyes:
            if enemy.life:
                enemy.render(screen)
                enemy.move(screen)
                if enemy.atack(screen, player.cords):
                    enemy.do_attack(screen)
                    player.heart -= 1

        
        if player.isfinish(screen, finish):
            screen.blit(shadow, (0, 0))
            result = win_render(screen, fps, clock, level_n, 3 * player.heart // 8)
            player.score += 100 *  player.heart // 8
            if result - level_n == 1:
                update(level_n, player.score, id_n, 3 * player.heart // 8)
            running = False
        
        if pause:
            screen.blit(shadow, (0, 0))
            menu_render(screen, fps, clock)
            pause = False

        if player.heart < 1:
            result = lose_render(screen, fps, clock, level_n)
            running = False

        pygame.display.flip()
        clock.tick(fps)
    return result