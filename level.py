import pygame
from settings import WIDTH, HEIGHT

class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.background = None
        self.floor_y = HEIGHT - 120  # Default floor height
        self.enemy_types = []
        self.wave_count = 3
        self.goal_item = None
        self.music = None
        self.load_level_data()

    def load_level_data(self):
        if self.level_number == 1:
            self.background = pygame.image.load("assets/images/level1_bg.jpg")
            self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
            self.floor_y = HEIGHT - 120
            self.enemy_types = ["orc", "goblin"]
            self.wave_count = 3
            self.goal_item = "Sunstone"
            self.music = "assets/sounds/level1_theme.mp3"

        elif self.level_number == 2:
            self.background = pygame.image.load("assets/images/level2_bg.jpg")
            self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
            self.floor_y = HEIGHT - 100
            self.enemy_types = ["skeleton", "bat"]
            self.wave_count = 4
            self.goal_item = "Moonstone"
            self.music = "assets/sounds/level2_theme.mp3"

    def get_background(self):
        return self.background

    def get_floor_y(self):
        return self.floor_y

    def get_enemy_types(self):
        return self.enemy_types

    def get_wave_count(self):
        return self.wave_count

    def get_goal_item(self):
        return self.goal_item

    def get_music(self):
        return self.music
