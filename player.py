
# player.py

import pygame
from settings import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = PLAYER_SPEED
        self.color = PLAYER_COLOR
        self.health = 3
        self.last_direction = "right"

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.last_direction = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.last_direction = "right"
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for i in range(self.health):
            pygame.draw.rect(screen, (0, 255, 0), (10 + i * 30, 10, 20, 20))
