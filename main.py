# main 2.py

import pygame
import sys
from settings import *
from player import Player
from enemy import Enemy, spawn_wave
from menu import Menu
#from level import level

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sunstone")
clock = pygame.time.Clock()

# Load Background
background = pygame.image.load("assets/images/Castle Background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Game states
MENU = "menu"
ADVENTURE = "adventure"
CHALLENGE = "challenge"
EQUIPMENT = "equipment"

# Create menu instance
menu = Menu(screen)

# Main application loop
while True:
    game_state = menu.run()

    if game_state in [ADVENTURE, CHALLENGE]:
        # Initialize game variables
        player = Player(WIDTH // 2, HEIGHT // 2)
        attack_timer = 0
        attack_rect = None
        wave = 1
        enemies = spawn_wave(wave)  # You can later split this into spawn_random_wave/spawn_fixed_wave

        # Game loop
        running = True
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            player.move(keys)

            if keys[pygame.K_SPACE] and attack_timer == 0:
                attack_timer = ATTACK_DURATION

            if attack_timer > 0:
                if player.last_direction == "right":
                    attack_rect = pygame.Rect(
                        player.rect.right,
                        player.rect.centery - ATTACK_HEIGHT // 2,
                        ATTACK_WIDTH,
                        ATTACK_HEIGHT
                    )
                else:
                    attack_rect = pygame.Rect(
                        player.rect.left - ATTACK_WIDTH,
                        player.rect.centery - ATTACK_HEIGHT // 2,
                        ATTACK_WIDTH,
                        ATTACK_HEIGHT
                    )
                attack_timer -= 1
            else:
                attack_rect = None

            for enemy in enemies:
                enemy.hit = False

            for enemy in enemies:
                enemy.update(player.rect)

                if enemy.alive and player.rect.colliderect(enemy.rect):
                    player.health -= 1
                    print(f"Knight hit! Health: {player.health}")
                    if player.last_direction == "right":
                        enemy.rect.x += PLAYER_WIDTH * 2
                    else:
                        enemy.rect.x -= PLAYER_WIDTH * 2

                    if player.health <= 0:
                        print("Game Over!")
                        running = False

                if attack_rect and enemy.alive and not enemy.hit and attack_rect.colliderect(enemy.rect):
                    enemy.health -= 1
                    enemy.hit = True
                    if player.last_direction == "right":
                        enemy.rect.x += PLAYER_WIDTH
                    else:
                        enemy.rect.x -= PLAYER_WIDTH
                    if enemy.health <= 0:
                        enemy.alive = False

            if all(not e.alive for e in enemies):
                wave += 1
                if wave <= 3:
                    enemies = spawn_wave(wave)
                else:
                    print("Victory! All waves completed.")
                    running = False

            screen.blit(background, (0, 0))
            player.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            if attack_rect:
                pass #pygame.draw.rect(screen, (255, 0, 0), attack_rect)

            pygame.display.flip()

    elif game_state == EQUIPMENT:
        # Placeholder for equipment screen
        print("Equipment screen not yet implemented.")
        pygame.time.wait(1000)  # Pause briefly before returning to menu
