import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Quest")

clock = pygame.time.Clock()
FPS = 60

# Player setup
player_width, player_height = 50, 70
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
player_color = (200, 50, 50)
last_direction = "right"
player_health = 3

# Attack setup
attack_width, attack_height = 50, 10
attack_duration = 20
attack_timer = 0
attack_rect = None

# Enemy setup
enemy_width, enemy_height = 50, 70
enemy_speed = 1.5
enemy_color = (50, 200, 50)

# Enemy wave tracking
enemies = []
wave = 0

def spawn_wave(wave):
    new_enemies = []
    if wave == 1:
        new_enemies.append({"x": 100, "y": 100, "health": 2, "alive": True})
    elif wave == 2:
        new_enemies.append({"x": WIDTH - 150, "y": 100, "health": 2, "alive": True})
    elif wave == 3:
        new_enemies.append({"x": 0, "y": 0, "health": 2, "alive": True})
        new_enemies.append({"x": WIDTH - enemy_width, "y": 0, "health": 2, "alive": True})
    return new_enemies

# Start with wave 1
wave = 1
enemies = spawn_wave(wave)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
        last_direction = "left"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
        last_direction = "right"
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_SPACE] and attack_timer == 0:
        attack_timer = attack_duration

    # Update attack
    if attack_timer > 0:
        attack_timer -= 1
        if last_direction == "right":
            attack_rect = pygame.Rect(player_x + player_width, player_y + player_height // 2 - attack_height // 2, attack_width, attack_height)
        else:
            attack_rect = pygame.Rect(player_x - attack_width, player_y + player_height // 2 - attack_height // 2, attack_width, attack_height)
    else:
        attack_rect = None

    # Keep player on screen
    player_x = max(0, min(WIDTH - player_width, player_x))
    player_y = max(0, min(HEIGHT - player_height, player_y))

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Enemy behavior
    for enemy in enemies:
        if enemy["alive"]:
            if enemy["x"] < player_x:
                enemy["x"] += enemy_speed
            elif enemy["x"] > player_x:
                enemy["x"] -= enemy_speed
            if enemy["y"] < player_y:
                enemy["y"] += enemy_speed
            elif enemy["y"] > player_y:
                enemy["y"] -= enemy_speed

            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], enemy_width, enemy_height)

            if player_rect.colliderect(enemy_rect):
                player_health -= 1
                print(f"Knight hit! Health: {player_health}")
                if last_direction == "right":
                    enemy["x"] += player_width * 2
                else:
                    enemy["x"] -= player_width * 2
                if player_health <= 0:
                    print("Game Over!")
                    running = False

            if attack_rect and attack_rect.colliderect(enemy_rect):
                enemy["health"] -= 1
                if last_direction == "right":
                    enemy["x"] += player_width
                else:
                    enemy["x"] -= player_width
                attack_rect = None
                if enemy["health"] <= 0:
                    enemy["alive"] = False

    # Check if all enemies are dead
    if all(not e["alive"] for e in enemies):
        wave += 1
        if wave <= 3:
            enemies = spawn_wave(wave)

    # Draw everything
    screen.fill((30, 30, 100))
    pygame.draw.rect(screen, player_color, player_rect)
    for enemy in enemies:
        if enemy["alive"]:
            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], enemy_width, enemy_height)
            pygame.draw.rect(screen, enemy_color, enemy_rect)
            for i in range(enemy["health"]):
                pygame.draw.rect(screen, (255, 0, 0), (enemy["x"] + i * 10, enemy["y"] - 10, 8, 8))
    if attack_rect:
        pygame.draw.rect(screen, (255, 0, 0), attack_rect)
    for i in range(player_health):
        pygame.draw.rect(screen, (0, 255, 0), (10 + i * 30, 10, 20, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()
