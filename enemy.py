
# enemy.py

import pygame
from settings import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_COLOR, ENEMY_SPEED

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.color = ENEMY_COLOR
        self.speed = ENEMY_SPEED
        self.health = 2
        self.alive = True
        self.hit = False

    def update(self, player_rect):
        if not self.alive:
            return
        if self.rect.x < player_rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player_rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player_rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player_rect.y:
            self.rect.y -= self.speed

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)
            for i in range(self.health):
                pygame.draw.rect(screen, (255, 0, 0), (self.rect.x + i * 10, self.rect.y - 10, 8, 8))

def spawn_wave(wave):
    from settings import WIDTH
    enemies = []
    if wave == 1:
        enemies.append(Enemy(100, 100))
    elif wave == 2:
        enemies.append(Enemy(WIDTH - 150, 100))
    elif wave == 3:
        enemies.append(Enemy(0, 0))
        enemies.append(Enemy(WIDTH - ENEMY_WIDTH, 0))
    return enemies
