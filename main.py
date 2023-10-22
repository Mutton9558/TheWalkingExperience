import pygame
from sys import exit
import math
from datetime import datetime

today = datetime.today()
d2 = today.strftime("%B %d, %Y %H:%M:%S")

def gameSetUp():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('The Walking Experience')
    clock = pygame.time.Clock()
    font = pygame.font.Font('font/Pixeltype.ttf', 40)
    game_active = True
    is_paused = False  # Add a variable to track if the game is paused

    character = pygame.Surface((25, 25))
    character.fill('Red')
    character_rect = character.get_rect(topleft=(10, 200))
    character_gravity = 0

    enemy = pygame.Surface((25, 25))
    enemy.fill('Purple')
    enemy_rect = enemy.get_rect(topleft=(700, 200))

    sky = pygame.image.load('images/image.png').convert_alpha()
    ground = pygame.image.load('images/ground.png').convert_alpha()

    stage1 = font.render('Myrum Valleys', False, 'White')
    stage1_rect = stage1.get_rect(center=(400, 135))

    def pause_menu():
        # Display the pause menu
        nonlocal is_paused
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                # Toggle fullscreen mode
                    pygame.display.toggle_fullscreen()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p: 
                        is_paused = False

            center_x = screen.get_width() // 2
            center_y = screen.get_height() // 2

            screen.fill('Black')
            pause_text = font.render('Paused', True, (255, 255, 255))
            resume_text = font.render('Resume (P)', True, (255, 255, 255))
            quit_text = font.render('Quit (Q)', True, (255, 255, 255))

            pause_text_rect = pause_text.get_rect(center=(center_x, center_y - 50))
            resume_text_rect = resume_text.get_rect(center=(center_x, center_y))
            quit_text_rect = quit_text.get_rect(center=(center_x, center_y + 50))

            screen.blit(pause_text, pause_text_rect)
            screen.blit(resume_text, resume_text_rect)
            screen.blit(quit_text, quit_text_rect)

            pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
            # Check for the fullscreen toggle event
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                # Toggle fullscreen mode
                    pygame.display.toggle_fullscreen()

            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and character_rect.bottom >= 225:
                        character_gravity = -10
                    elif event.key == pygame.K_ESCAPE:  # Press 'ESC' to pause the game
                        is_paused = True
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rect.left = 700
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        pygame.quit()
                        exit()

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
            screen.fill('Black')
            # Display a game-over screen
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            restart_text = font.render("Press SPACE to Restart", True, (255, 255, 255))
            exit_text = font.render("Press E to Exit", True, (255, 255, 255))

            game_over_rect = game_over_text.get_rect(center=(400, 150))
            restart_rect = restart_text.get_rect(center=(400, 250))
            exit_rect = exit_text.get_rect(center=(400, 300))

            screen.blit(game_over_text, game_over_rect)
            screen.blit(restart_text, restart_rect)
            screen.blit(exit_text, exit_rect)

        if is_paused:
            pause_menu()  # Display the pause menu

        pygame.display.update()
        clock.tick(60)

gameSetUp()

# tips for future ref
# pygame.image.load('file path')
