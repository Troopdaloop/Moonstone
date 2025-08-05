import pygame

class Scaler:
    def __init__(self, base_resolution, current_resolution, enable_letterboxing=False):
        self.base_width, self.base_height = base_resolution
        self.screen_width, self.screen_height = current_resolution
        self.enable_letterboxing = enable_letterboxing

        scale_x = self.screen_width / self.base_width
        scale_y = self.screen_height / self.base_height
        self.scale = min(scale_x, scale_y)

        self.scaled_width = int(self.base_width * self.scale)
        self.scaled_height = int(self.base_height * self.scale)

        self.offset_x = (self.screen_width - self.scaled_width) // 2 if enable_letterboxing else 0
        self.offset_y = (self.screen_height - self.scaled_height) // 2 if enable_letterboxing else 0

    def scale_image(self, image):
        """Scales a Pygame surface (e.g., sprite or background)."""
        width = int(image.get_width() * self.scale)
        height = int(image.get_height() * self.scale)
        return pygame.transform.scale(image, (width, height))

    def scale_position(self, pos):
        """Scales a position tuple (x, y)."""
        x, y = pos
        return (
            int(x * self.scale) + self.offset_x,
            int(y * self.scale) + self.offset_y
        )

    def scale_rect(self, rect):
        """Scales a Pygame Rect object."""
        return pygame.Rect(
            int(rect.x * self.scale) + self.offset_x,
            int(rect.y * self.scale) + self.offset_y,
            int(rect.width * self.scale),
            int(rect.height * self.scale)
        )
