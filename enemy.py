import os
import pygame
from settings import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_COLOR, ENEMY_SPEED

class BatEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = self.load_frames("assets/images/Enemies/Bat1/Fly")
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_speed = 0.2
        self.health = 2
        self.alive = True
        self.hit = False

    def load_frames(self, folder):
        frames = []
        for filename in sorted(os.listdir(folder)):
            if filename.endswith(".png"):
                img = pygame.image.load(os.path.join(folder, filename)).convert_alpha()
                img = pygame.transform.scale(img, (ENEMY_WIDTH, ENEMY_HEIGHT))
                frames.append(img)
        return frames

    def update(self, player_rect):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

        if not self.alive:
            return
        if self.rect.x < player_rect.x:
            self.rect.x += ENEMY_SPEED
        elif self.rect.x > player_rect.x:
            self.rect.x -= ENEMY_SPEED
        if self.rect.y < player_rect.y:
            self.rect.y += ENEMY_SPEED
        elif self.rect.y > player_rect.y:
            self.rect.y -= ENEMY_SPEED

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
            for i in range(self.health):
                pygame.draw.rect(screen, (255, 0, 0), (self.rect.x + i * 10, self.rect.y - 10, 8, 8))

def spawn_wave(wave):
    from settings import WIDTH
    enemies = []
    if wave == 1:
        enemies.append(BatEnemy(100, 100))
    elif wave == 2:
        enemies.append(BatEnemy(WIDTH - 150, 100))
    elif wave == 3:
        enemies.append(BatEnemy(0, 0))
        enemies.append(BatEnemy(WIDTH - ENEMY_WIDTH, 0))
    return enemies
