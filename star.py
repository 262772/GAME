import pygame

class Stars(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/BACKGROUND_ITEMS/star.gif").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

STARS = pygame.sprite.Group()
