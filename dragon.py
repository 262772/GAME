import random
import pygame
from parameters import *
class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/CHARACTERS/dragon2.gif").convert()
        self.image.set_colorkey((0, 0, 0))
        self.flip = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_DRAGON_SPEED, MAX_DRAGON_SPEED)
        self.rect.center = (x, y)

    def update(self, screen):
        self.y -= self.speed
        self.rect.y = self.y
    def draw(self, screen):
        screen.blit(self.image, self.rect)


DRAGONS = pygame.sprite.Group()



