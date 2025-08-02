import pygame
import os
from settings import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = PLAYER_SPEED
        self.health = 3
        self.last_direction = "right"

        # Load walk frames
        self.walk_frames = []
        walk_folder = "assets/images/Player/BlueKnight/Walk/player_frames"
        for i in range(10):
            path = os.path.join(walk_folder, f"frame_{i}.png")
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
            self.walk_frames.append(img)

        # Load idle frames
        self.idle_frames = []
        idle_folder = "assets/images/Player/BlueKnight/Idle/player_frames"
        for i in range(10):
            path = os.path.join(idle_folder, f"frame_{i}.png")
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
            self.idle_frames.append(img)

        # Load attack frames
        self.attack_frames = []
        attack_folder = "assets/images/Player/BlueKnight/Attack1/player_frames"
        for i in range(10):
            path = os.path.join(attack_folder, f"frame_{i}.png")
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
            self.attack_frames.append(img)

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 5
        self.is_moving = False
        self.is_attacking = False

    def move(self, keys):
        self.is_moving = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.last_direction = "left"
            self.is_moving = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.last_direction = "right"
            self.is_moving = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.is_moving = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.is_moving = True
        if keys[pygame.K_SPACE]:
            self.is_attacking = True
            self.current_frame = 0
            self.frame_timer = 0

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, screen):
        # Animate
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_frame += 1

        if self.is_attacking:
            frames = self.attack_frames
            if self.current_frame >= len(frames):
                self.current_frame = 0
                self.is_attacking = False
        else:
            frames = self.walk_frames if self.is_moving else self.idle_frames
            self.current_frame %= len(frames)

        frame = frames[self.current_frame]

        # Flip if facing right (sprite faces left by default)
        if self.last_direction == "right":
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, self.rect.topleft)

        # Draw health
        for i in range(self.health):
            pygame.draw.rect(screen, (0, 255, 0), (10 + i * 30, 10, 20, 20))
