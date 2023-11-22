import pygame
import sys
import random
from parameters import *
from background import draw_background
from batman import Batman, HEROES
from player import Player
from dragon import Dragon, DRAGONS
#initiate game
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding all characters')

# create clock
clock = pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

#add_batman(5)

#add_groot(5)

for _ in range(3):
    HEROES.add(Batman(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*10), random.randint(TILE_SIZE, SCREEN_HEIGHT-2*TILE_SIZE)))
for _ in range(4):
    DRAGONS.add(Dragon(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 10), random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

#create knight
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        # control knight with keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()

        if event.type == pygame.KEYUP:
            player.stop()
    screen.blit(background, (0, 0))

    HEROES.update(screen)
    DRAGONS.update(screen)
    player.update()

    # check if batman is off the screen
    for batman in HEROES:
        if batman.rect.x < -batman.rect.width+100:  # use the tile size
            HEROES.remove(batman)  # remove the fish from the sprite group
            HEROES.add(Batman(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

        for dragon in DRAGONS:
            if dragon.rect.y < -dragon.rect.height+100:  # use the tile size
                dragon.rect.y = -dragon.rect.y
            if dragon.rect.y < -dragon.rect.height+ SCREEN_HEIGHT - 100:
                dragon.rect.y = dragon.rect.y
                #DRAGONS.remove(dragon)  # remove the fish from the sprite group
                #DRAGONS.add(Dragon(random.randint(LAVA_TILE_SIZE+50, SCREEN_WIDTH),
                           # random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT)))

    #draw characters on screen
    HEROES.draw(screen)
    player.draw(screen)
    DRAGONS.draw(screen)
    #update display of the game
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

screen.blit(background, (0,0))

pygame.display.flip()

pygame.quit()
sys.exit()
