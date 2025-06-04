"""
Pipe class for the FlappyPy game.
"""
import pygame
import random
from .constants import (
    PIPE_WIDTH, PIPE_GAP, PIPE_SPEED,
    WINDOW_HEIGHT, WINDOW_WIDTH, GREEN
)


class Pipe:
    def __init__(self):
        self.width = PIPE_WIDTH
        self.gap = PIPE_GAP
        self.speed = PIPE_SPEED
        self.x = WINDOW_WIDTH
        self.passed = False

        # Randomly generate gap position
        self.gap_y = random.randint(100, WINDOW_HEIGHT - 100)

        # Create rectangles for top and bottom pipes
        self.top_height = self.gap_y - self.gap // 2
        self.bottom_height = WINDOW_HEIGHT - (self.gap_y + self.gap // 2)

        self.top_rect = pygame.Rect(
            self.x, 0,
            self.width, self.top_height
        )
        self.bottom_rect = pygame.Rect(
            self.x, self.gap_y + self.gap // 2,
            self.width, self.bottom_height
        )

    def update(self):
        """Update pipe position."""
        self.x -= self.speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        """Draw the pipes on the screen."""
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

    def is_off_screen(self):
        """Check if pipe has moved off screen."""
        return self.x < -self.width

    def collides_with(self, bird_rect):
        """Check if bird collides with either pipe."""
        return (self.top_rect.colliderect(bird_rect) or
                self.bottom_rect.colliderect(bird_rect))
