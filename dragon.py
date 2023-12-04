import random
import pygame
from parameters import *
class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/CHARACTERS/dragon2.gif").convert()
        self.image.set_colorkey((0, 0, 0))
        self.reverse = pygame.transform.flip(self.image, True, False)
        self.forward = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_DRAGON_SPEED, MAX_DRAGON_SPEED)
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = random.uniform(MIN_DRAGON_SPEED, MAX_DRAGON_SPEED)

    def update(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        # boundaries for fire monster to move up and down and not touch water
        if self.y > SCREEN_HEIGHT-(TILE_SIZE+WATER_TILE_SIZE):
            self.y_speed = -1*self.y_speed
            self.image = self.forward
        if self.y < 66:
            self.y_speed = -1*self.y_speed
            self.image = self.reverse
        self.y += self.y_speed



    def draw(self, screen):

        screen.blit(self.image, self.rect)


DRAGONS = pygame.sprite.Group()



