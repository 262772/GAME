import pygame
import sys
import random
from parameters import *
from background import draw_background, draw_background2, add_batman, add_titan, add_star, remove_titan, remove_star, add_dragon, remove_dragon, remove_batman
from batman import Batman, HEROES
from player import Player
from dragon import Dragon, DRAGONS
from pet import Pet
from Titan import COLLECT
from star import STARS

#initiate game
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding all characters')

# create clock
clock = pygame.time.Clock()

running = True

#draw background
background = screen.copy()
draw_background(background)
#add character and items capable of being added/removed
add_batman(2)

add_titan(1)

add_star(1)

#add fire monster to screen
for _ in range(1):
    DRAGONS.add(Dragon(140, SCREEN_HEIGHT-WATER_TILE_SIZE*2))
    DRAGONS.add(Dragon(290, SCREEN_HEIGHT-WATER_TILE_SIZE*2))
    DRAGONS.add(Dragon(440, SCREEN_HEIGHT-WATER_TILE_SIZE*2))
    DRAGONS.add(Dragon(590, SCREEN_HEIGHT-WATER_TILE_SIZE*2))

#create player and pet
player = Player(SCREEN_WIDTH/2, 0)
pet = Pet(SCREEN_WIDTH/2, SCREEN_HEIGHT-TORCH_TILE_SIZE/2)

#sounds
im_batman = pygame.mixer.Sound("assets/SOUNDS/im_batman.mp3")
theme = pygame.mixer.Sound("assets/SOUNDS/attack_on_titan.mp3")
blaze = pygame.mixer.Sound("assets/SOUNDS/blaze.mp3")
titan_spawn = pygame.mixer.Sound("assets/SOUNDS/eren_yeager.mp3")
star = pygame.mixer.Sound("assets/SOUNDS/twinkle.mp3")

#heart images
red_heart = pygame.image.load("assets/BACKGROUND_ITEMS/player_heart.gif").convert()
pink_heart = pygame.image.load("assets/BACKGROUND_ITEMS/pet_heart.gif").convert()
red_heart.set_colorkey((255, 255, 255))
pink_heart.set_colorkey((0, 0, 0))

#set score default as zero
score = 0
power_score = 0

score_font = pygame.font.Font("assets/FONTS/Black_Crayon.ttf", 30)
endgame_font = pygame.font.Font("assets/FONTS/Black_Crayon.ttf", 64)

player_lives = PLAYER_LIVES
pet_lives = PET_LIVES

#once either life = 0 the game will stop running and blit to game over
while player_lives > 0 and pet_lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control player and pet with keyboard
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pet.move_up()
            if event.key == pygame.K_s:
                pet.move_down()
            if event.key == pygame.K_a:
                pet.move_left()
            if event.key == pygame.K_d:
                pet.move_right()

        if event.type == pygame.KEYUP:
            pet.stop()
    #blits the "background" screen onto the pygame while it runs
    screen.blit(background, (0, 0))

    #updates the batman,firemonster, pet, and player movements and pet and player onto screen
    HEROES.update(screen)
    DRAGONS.update(screen)
    player.update()
    pet.update()

    #pygame.mixer.Sound.play(theme)

    # check for player collisions
    result1 = pygame.sprite.spritecollide(player, HEROES, True)
    result2 = pygame.sprite.spritecollide(player, DRAGONS, True)
    result3 = pygame.sprite.spritecollide(player, COLLECT, False)

    # check for pet collisions
    result4 = pygame.sprite.spritecollide(pet, HEROES, True)
    result5 = pygame.sprite.spritecollide(pet, DRAGONS, True)
    result6 = pygame.sprite.spritecollide(pet, STARS, False)

    if result1:
        # play batman sound
        pygame.mixer.Sound.play(im_batman)
        remove_batman(1)
        # adds more batman when less lives are available
        add_batman(6-player_lives)
        # takes away life from player
        player_lives -= len(result1)

    if result2:
        # play fire sound
        pygame.mixer.Sound.play(blaze)
        player_lives -= len(result2)
        # colliding with fire monster decreases a life of player
        remove_dragon(1)
        add_dragon(1)

    if result3:
        # play lightning sound
        pygame.mixer.Sound.play(titan_spawn)
        score +=len(result3)
        # as power score increases more titans are available to kill and add to score
        remove_titan(power_score+1)
        add_titan(power_score+1)

    if result4:
        pygame.mixer.Sound.play(im_batman)
        pet_lives -= len(result4)
        remove_batman(1)
        add_batman(6-pet_lives)

    if result5:
        pygame.mixer.Sound.play(blaze)
        remove_dragon(1)
        add_dragon(1)

        pet_lives -= len(result5)

    if result6:
        pygame.mixer.Sound.play(star)
        power_score += len(result6)
        # pet colliding with star adds to power score
        remove_star(1)
        add_star(1)
        # adds an extra titan to the screen for player to have more options to kill
        add_titan(1)

        #PLAYER_SPEED += 10
    #player.update()
    #if HEROES == 0:
        #add_batman(1)



    # check if batman is off the screen and respawn him
    for batman in HEROES:
        if batman.rect.x < -batman.rect.width+100:  # use the tile size
            HEROES.remove(batman)  # remove the fish from the sprite group
            HEROES.add(Batman(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(WATER_TILE_SIZE*1.25, SCREEN_HEIGHT - WATER_TILE_SIZE*1.25)))

    # drawing all the images with collisions on the screen
    COLLECT.draw(screen)
    STARS.draw(screen)
    DRAGONS.draw(screen)
    HEROES.draw(screen)
    player.draw(screen)
    pet.draw(screen)


    #bliting the player and power score NUMBERS on the screen
    text = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH - 45, 65))

    text2 = score_font.render(f"{power_score}", True, (255, 192, 203))
    screen.blit(text2, (SCREEN_WIDTH - 45, 100))

    #bliting the number of heart images of player and pet on the screen
    for i in range(pet_lives):
        screen.blit(pink_heart, (i * TILE_SIZE + 325, 475))

    for i in range(player_lives):
        screen.blit(red_heart, (i * TILE_SIZE + 325, 400))

    #update display of the game
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

#create new background when either lives == 0
screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background2 = screen1.copy()
draw_background2(background2)
screen1.blit(background2, (0, 0))

#show game over message
message = endgame_font.render("GAME OVER", True, (255, 255, 255))
screen.blit(message, (SCREEN_WIDTH-565, SCREEN_HEIGHT-400))

#show final score
score_text = endgame_font.render(f"Score: {score}", True, (255, 255, 255))
screen.blit(score_text, (SCREEN_WIDTH-565, SCREEN_HEIGHT-325))

pygame.display.flip()

#when pressing quit on the game over screen, the pygame quits
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
