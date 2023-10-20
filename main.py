import pygame
from sys import exit
import math
from datetime import datetime

today = datetime.today()
d2 = today.strftime("%B %d, %Y %H:%M:%S")

def gameSetUp():
    # initialises PyGame
    pygame.init()
    # creates display
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('The Walking Experience')
    clock = pygame.time.Clock()
    font = pygame.font.Font('font/Pixeltype.ttf', 40)
    game_active = True

    character = pygame.Surface((25,25))
    character.fill('Red')
    character_rect = character.get_rect(topleft=(10,200))
    character_gravity = 0

    enemy = pygame.Surface((25,25))
    enemy.fill('Purple')
    enemy_rect = enemy.get_rect(topleft=(700,200))

    sky = pygame.image.load('images/image.png').convert_alpha()
    ground = pygame.image.load('images/ground.png').convert_alpha()

    stage1 = font.render('Myrum Valleys', False, 'White')
    stage1_rect = stage1.get_rect(center=(400,135))

    while True:
        # closes app
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                # Check for the fullscreen toggle event
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                # Toggle fullscreen mode
                    pygame.display.toggle_fullscreen()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and character_rect.bottom >= 225:
                        character_gravity = -10
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rect.left = 700

        if game_active:
            # displays something in display     
            screen.blit(sky,(0,0))   
            screen.blit(ground, (0,225))

            character_gravity += 0.5
            character_rect.y += character_gravity
            if character_rect.bottom >= 225:
                character_rect.bottom = 225
            screen.blit(character,character_rect)

            enemy_rect.left -=1
            if enemy_rect.left <= -25:
                enemy_rect.left = -25
            screen.blit(enemy, enemy_rect)

            screen.blit(stage1, stage1_rect) 

            # game over
            if character_rect.colliderect(enemy_rect):
                game_active = False
        else:
            screen.fill('red')

        # draw elements
        # update
        pygame.display.update()
        clock.tick(60)

gameSetUp()

# tips for future ref
# pygame.image.load('file path')