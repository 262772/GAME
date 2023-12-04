
import random
import pygame
from parameters import *
class TITANS(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/BACKGROUND_ITEMS/eren.gif").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

COLLECT = pygame.sprite.Group()
