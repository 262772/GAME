import pygame
from parameters import *
import random

def draw_background(screen):
    #Load our tiles from the assets folder
    dungeon = pygame.image.load("assets/BACKGROUND_ITEMS/stone_wall.png").convert()
    torch = pygame.image.load("assets/BACKGROUND_ITEMS/torch.gif").convert()
    lava = pygame.image.load("assets/BACKGROUND_ITEMS/lava.jpg")
    eren = pygame.image.load("assets/BACKGROUND_ITEMS/eren.gif").convert()

    #make PNGS transparent

    dungeon.set_colorkey((0,0,0))
    torch.set_colorkey((255,255,255))
    eren.set_colorkey((0,0,0))


  #fill screen with stone background
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(dungeon, (x, y))

    #draw torch
    screen.blit(torch, ((TORCH_TILE_SIZE * 1)+10, 0))
    screen.blit(torch, (TORCH_TILE_SIZE * 3, 0))
    screen.blit(torch, (TORCH_TILE_SIZE * 5, 0))
    screen.blit(torch, (TORCH_TILE_SIZE * 7, 0))
    screen.blit(torch, (TORCH_TILE_SIZE * 9, 0))


    screen.blit(torch, ((TORCH_TILE_SIZE * 1)+10, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 3, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 5, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 7, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 9, SCREEN_HEIGHT - TORCH_TILE_SIZE))

    screen.blit(lava, (0, LAVA_TILE_SIZE*0))
    screen.blit(lava, (0, LAVA_TILE_SIZE*1))
    screen.blit(lava, (0, LAVA_TILE_SIZE*2))
    screen.blit(lava, (0, LAVA_TILE_SIZE*3))
    screen.blit(lava, (0, LAVA_TILE_SIZE*4))
    screen.blit(lava, (0, LAVA_TILE_SIZE*5))

    for _ in range(2):
        x = random.randint(1.5*LAVA_TILE_SIZE, SCREEN_WIDTH - LAVA_TILE_SIZE*0.5)
        y = random.randint(TILE_SIZE*2, SCREEN_HEIGHT - 2*TILE_SIZE)
        screen.blit(eren, (x, y))
    #screen.blit(groot, random.randint(1.5*LAVA_TILE_SIZE, SCREEN_WIDTH - LAVA_TILE_SIZE*0.5),
                       #     random.randint(TILE_SIZE*2, SCREEN_HEIGHT - 2*TILE_SIZE))))

    #custom_font = pygame.font.Font("assests/FONTS/Black_Crayon.ttf", 48)
    #text = custom_font.render("Dungeon Slayer", True, (136, 8, 8))
    #screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))