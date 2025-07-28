# main 2.py

import pygame
import sys
from settings import *
from player import Player
from enemy import Enemy, spawn_wave
from menu import Menu

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sunstone")
clock = pygame.time.Clock()

# Game states
MENU = "menu"
PLAYING = "playing"

# Create menu instance
menu = Menu(screen)

# Main application loop
while True:
    # Show the menu and wait for user input
    game_state = menu.run()

    # If the player chooses to start the game
    if game_state == PLAYING:
        # Initialize game variables
        player = Player(WIDTH // 2, HEIGHT // 2)
        attack_timer = 0
        attack_rect = None
        wave = 1
        enemies = spawn_wave(wave)

        # Game loop
        running = True
        while running:
            clock.tick(FPS)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Handle player movement
            keys = pygame.key.get_pressed()
            player.move(keys)

            # Handle attack input
            if keys[pygame.K_SPACE] and attack_timer == 0:
                attack_timer = ATTACK_DURATION
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

            # Update attack timer
            if attack_timer > 0:
                attack_timer -= 1
            else:
                attack_rect = None

            # Reset enemy hit flags
            for enemy in enemies:
                enemy.hit = False

            # Update enemies and check collisions
            for enemy in enemies:
                enemy.update(player.rect)

                # Check if enemy collides with player
                if enemy.alive and player.rect.colliderect(enemy.rect):
                    player.health -= 1
                    print(f"Knight hit! Health: {player.health}")
                    if player.last_direction == "right":
                        enemy.rect.x += PLAYER_WIDTH * 2
                    else:
                        enemy.rect.x -= PLAYER_WIDTH * 2

                    # Check for player death
                    if player.health <= 0:
                        print("Game Over!")
                        running = False  # Exit game loop to return to menu

                # Check if enemy is hit by attack
                if attack_rect and enemy.alive and not enemy.hit and attack_rect.colliderect(enemy.rect):
                    enemy.health -= 1
                    enemy.hit = True
                    if player.last_direction == "right":
                        enemy.rect.x += PLAYER_WIDTH
                    else:
                        enemy.rect.x -= PLAYER_WIDTH
                    if enemy.health <= 0:
                        enemy.alive = False

            # Check if all enemies are defeated
            if all(not e.alive for e in enemies):
                wave += 1
                if wave <= 3:
                    enemies = spawn_wave(wave)
                else:
                    print("Victory! All waves completed.")
                    running = False  # Exit game loop to return to menu

            # Draw everything
            screen.fill(BG_COLOR)
            player.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            if attack_rect:
                pygame.draw.rect(screen, (255, 0, 0), attack_rect)

            pygame.display.flip()
