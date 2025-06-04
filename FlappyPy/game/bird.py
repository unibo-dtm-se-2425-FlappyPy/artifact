"""
Bird class for the FlappyPy game.
"""
import pygame
from .constants import (
    BIRD_WIDTH, BIRD_HEIGHT, BIRD_START_X, BIRD_START_Y,
    GRAVITY, JUMP_STRENGTH, WINDOW_HEIGHT
)


class Bird:
    def __init__(self):
        self.x = BIRD_START_X
        self.y = BIRD_START_Y
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        """Make the bird jump."""
        self.velocity = JUMP_STRENGTH

    def update(self):
        """Update bird position and velocity."""
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity

        # Update rectangle position
        self.rect.y = self.y

        # Prevent bird from going off screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > WINDOW_HEIGHT - self.height:
            self.y = WINDOW_HEIGHT - self.height
            self.velocity = 0

    def draw(self, screen):
        """Draw the bird on the screen."""
        pygame.draw.rect(screen, (255, 255, 0),
                         self.rect)  # Yellow color for the bird

    def reset(self):
        """Reset bird to initial position."""
        self.y = BIRD_START_Y
        self.velocity = 0
        self.rect.y = self.y
