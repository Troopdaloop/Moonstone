
import pygame
import sys
from settings import WIDTH, HEIGHT, BG_COLOR

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 60)
        self.options = ["Adventure", "Challenge", "Equipment", "Quit"]
        self.selected = 0

    def draw(self):
        self.screen.fill(BG_COLOR)
        title = self.font.render("Sunstone", True, (255, 255, 255))
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (255, 255, 255)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 250 + i * 80))

        pygame.display.flip()

    def run(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        selected = self.options[self.selected]
                        if selected == "Adventure":
                            return "adventure"
                        elif selected == "Challenge":
                            return "challenge"
                        elif selected == "Equipment":
                            return "equipment"
                        elif selected == "Quit":
                            pygame.quit()
                            sys.exit()
