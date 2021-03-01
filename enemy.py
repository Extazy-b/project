import pygame
import config


class Enemy():
    def __init__(self, info):
        self.start, self.amplitude, self.orient = info
        self.start = [(config.indent + (self.start[0] * config.CELL_SIZE)), 
                      (config.indent + (self.start[1] * config.CELL_SIZE))]

        self.amplitude *= config.CELL_SIZE
        self.r = 20
        self.cords = self.start[:]
        self.delta = 1
        self.attak = True
        self.life = True

        self.image = pygame.image.load(f"image/enemy_{self.orient}.png")
        self.fire = pygame.image.load(f"image/fire_{self.orient}.jpg")

        self.image.set_colorkey((255, 255, 255))
        self.fire.set_colorkey((255, 255, 255))

    def render(self, screen):
        #pygame.draw.circle(screen, (255, 0, 0), self.cords, 25)
        screen.blit(self.image, (self.cords[0] - (config.CELL_SIZE * 0.75), 
                                 self.cords[1] - (config.CELL_SIZE * 0.75)))
        if not self.attak:
            self.do_attack(screen)

    def move(self, screen):
        self.cords[self.orient] += self.delta
        if self.cords[self.orient] > self.start[self.orient] + self.amplitude:
            self.image = pygame.transform.flip(self.image, 1 - self.orient, self.orient)
            self.fire = pygame.transform.flip(self.fire, 1 - self.orient, self.orient)

            self.fire.set_colorkey((255, 255, 255))
            self.image.set_colorkey((255, 255, 255))
            self.delta *= -1
            self.attak = True

        if self.cords[self.orient] < self.start[self.orient]:
            self.image = pygame.transform.flip(self.image, 1 - self.orient, self.orient)
            self.fire = pygame.transform.flip(self.fire, 1 - self.orient, self.orient)
            
            self.fire.set_colorkey((255, 255, 255))
            self.image.set_colorkey((255, 255, 255))
            self.delta *= -1
            self.attak = True
    
    def atack(self, screen, hero_pos):
        rull_1 = hero_pos[self.orient] in range(self.cords[self.orient],
                                                self.cords[self.orient] + (self.delta * 25), 
                                                self.delta)
        rull_2 = hero_pos[1 - self.orient] in range(self.cords[1 - self.orient] - self.r,
                                                    self.cords[1 - self.orient] + self.r)

        if (self.attak and rull_1 and rull_2):
            self.attak = False
            return True


    def do_attack(self, screen):
        x = self.cords[1 - self.orient] - 20
        y = self.cords[self.orient] + (self.r * self.delta) - 20 * bool(1 - self.delta)
        (x, y) = (y, x) if not self.orient else (x, y)
        screen.blit(self.fire, (x, y))
