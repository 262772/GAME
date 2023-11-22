import random
import pygame
from parameters import *
class GROOT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/CHARACTERS/GROOT.jpg").convert()
        self.image.set_colorkey((0, 0, 0))
        #self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_BATMAN_SPEED, MAX_BATMAN_SPEED)
        self.rect.center = (x, y)
    def update(self, screen):
        self.x -= self.speed
        self.rect.x = self.x
    def draw(self, screen):
        screen.blit(self.image, self.rect)


GROOTS = pygame.sprite.Group()