import pygame
from parameters import *
import random
from batman import Batman, HEROES
from Titan import TITANS, COLLECT
from star import STARS, Stars
from dragon import DRAGONS, Dragon

def draw_background(screen):
    #Load background items from the assets folder
    dungeon = pygame.image.load("assets/BACKGROUND_ITEMS/stone_wall.png").convert()
    torch = pygame.image.load("assets/BACKGROUND_ITEMS/torch.gif").convert()
    lava = pygame.image.load("assets/BACKGROUND_ITEMS/lava.jpg")
    eren = pygame.image.load("assets/BACKGROUND_ITEMS/eren.gif").convert()
    water = pygame.image.load("assets/BACKGROUND_ITEMS/water.png")

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

    #draw water
    screen.blit(water, (LAVA_TILE_SIZE + 0.5*TORCH_TILE_SIZE + 10, -25))
    screen.blit(water, (LAVA_TILE_SIZE + 2.5*TORCH_TILE_SIZE, -25))
    screen.blit(water, (LAVA_TILE_SIZE + 4.5*TORCH_TILE_SIZE, -25))
    screen.blit(water, (LAVA_TILE_SIZE + 6.5*TORCH_TILE_SIZE, -25))

    screen.blit(water, (LAVA_TILE_SIZE + 0.5 * TORCH_TILE_SIZE + 10, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(water, (LAVA_TILE_SIZE + 2.5 * TORCH_TILE_SIZE, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(water, (LAVA_TILE_SIZE + 4.5 * TORCH_TILE_SIZE, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(water, (LAVA_TILE_SIZE + 6.5 * TORCH_TILE_SIZE, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    #draw torch under
    screen.blit(torch, ((TORCH_TILE_SIZE * 1)+10, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 3, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 5, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 7, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    screen.blit(torch, (TORCH_TILE_SIZE * 9, SCREEN_HEIGHT - TORCH_TILE_SIZE))
    #draw lava tiles
    screen.blit(lava, (0, LAVA_TILE_SIZE*0))
    screen.blit(lava, (0, LAVA_TILE_SIZE*1))
    screen.blit(lava, (0, LAVA_TILE_SIZE*2))
    screen.blit(lava, (0, LAVA_TILE_SIZE*3))
    screen.blit(lava, (0, LAVA_TILE_SIZE*4))
    screen.blit(lava, (0, LAVA_TILE_SIZE*5))


    # fonts
    custom_font = pygame.font.Font("assets/FONTS/Black_Crayon.ttf", 48)
    text_font = pygame.font.Font("assets/FONTS/Roboto_Medium.ttf", 24)

    # text to indicate player/pet lives/score/game title
    text = custom_font.render("Dungeon Slayer", True, (136, 8, 8))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, TORCH_TILE_SIZE))

    player_score = text_font.render("Player Score:", True, (255, 0, 0))
    screen.blit(player_score, (SCREEN_WIDTH - 215, 65))

    power_score = text_font.render("Power Score:", True, (255, 192, 203))
    screen.blit(power_score, (SCREEN_WIDTH - 215, 100))

    player_hearts = text_font.render("Player Hearts:", True, (255, 0, 0))
    screen.blit(player_hearts, (SCREEN_WIDTH - 650, 405))

    pet_hearts = text_font.render("Power Score:", True, (255, 192, 203))
    screen.blit(pet_hearts, (SCREEN_WIDTH - 650, 475))


#adding function for enemies and collectables
def add_batman(num_batman):
    for _ in range(num_batman):
        HEROES.add(Batman(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50), random.randint(WATER_TILE_SIZE*1.25, SCREEN_HEIGHT - WATER_TILE_SIZE*1.25)))

def add_titan(num_titan):
    for _ in range(num_titan):
        COLLECT.add(TITANS(random.randint(1.5*LAVA_TILE_SIZE, SCREEN_WIDTH - LAVA_TILE_SIZE*0.5), random.randint(TILE_SIZE*2, SCREEN_HEIGHT - 2*TILE_SIZE)))

def add_star(num_star):
    for _ in range(num_star):
        STARS.add(Stars(random.randint(1.5*LAVA_TILE_SIZE, SCREEN_WIDTH - LAVA_TILE_SIZE*0.5), random.randint(TILE_SIZE*2, SCREEN_HEIGHT - 2*TILE_SIZE)))
def add_dragon(num_dragon):
    for _ in range(num_dragon):
        DRAGONS.add(Dragon(140, SCREEN_HEIGHT-WATER_TILE_SIZE*2))
        DRAGONS.add(Dragon(290, SCREEN_HEIGHT - WATER_TILE_SIZE * 2))
        DRAGONS.add(Dragon(440, SCREEN_HEIGHT - WATER_TILE_SIZE * 2))
        DRAGONS.add(Dragon(590, SCREEN_HEIGHT - WATER_TILE_SIZE * 2))


#removing function for enemies and collectables

def remove_titan(num_titan):
    for _ in range(num_titan):
        for titan in COLLECT:
            COLLECT.remove(titan)

def remove_star(num_star):
    for _ in range(num_star):
        for star in STARS:
            STARS.remove(star)

def remove_dragon(num_dragon):
    for _ in range(num_dragon):
        for dragon in DRAGONS:
            DRAGONS.remove(dragon)

def remove_batman(num_batman):
    for _ in range(num_batman):
        for batman in HEROES:
            HEROES.remove(batman)

# function to draw the endgame background
def draw_background2(screen1):
    new_background = pygame.image.load("assets/BACKGROUND_ITEMS/new_background.jpg")
    screen1.blit(new_background, (0,0)),



