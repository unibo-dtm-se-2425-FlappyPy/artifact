"""
Main game class for FlappyPy.
"""
import pygame
import time
from .constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GAME_STATE_MENU, GAME_STATE_PLAYING, GAME_STATE_GAME_OVER,
    WHITE, BLACK
)
from .bird import Bird
from .pipe import Pipe


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("FlappyPy")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.reset_game()

    def reset_game(self):
        """Reset game state."""
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.game_state = GAME_STATE_MENU
        self.last_pipe_spawn = time.time() * 1000

    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_state == GAME_STATE_MENU:
                        self.game_state = GAME_STATE_PLAYING
                    elif self.game_state == GAME_STATE_PLAYING:
                        self.bird.jump()
                    elif self.game_state == GAME_STATE_GAME_OVER:
                        self.reset_game()
        return True

    def update(self):
        """Update game state."""
        if self.game_state != GAME_STATE_PLAYING:
            return

        # Update bird
        self.bird.update()

        # Spawn new pipes
        current_time = time.time() * 1000
        if current_time - self.last_pipe_spawn > 1500:  # Spawn every 1.5 seconds
            self.pipes.append(Pipe())
            self.last_pipe_spawn = current_time

        # Update pipes
        for pipe in self.pipes[:]:
            pipe.update()

            # Check for collisions
            if pipe.collides_with(self.bird.rect):
                self.game_state = GAME_STATE_GAME_OVER

            # Remove off-screen pipes
            if pipe.is_off_screen():
                self.pipes.remove(pipe)
                self.score += 1

    def draw(self):
        """Draw game elements."""
        self.screen.fill(WHITE)

        if self.game_state == GAME_STATE_MENU:
            text = self.font.render("Press SPACE to Start", True, BLACK)
            self.screen.blit(
                text, (WINDOW_WIDTH//2 - text.get_width()//2, WINDOW_HEIGHT//2))

        elif self.game_state == GAME_STATE_PLAYING:
            # Draw bird
            self.bird.draw(self.screen)

            # Draw pipes
            for pipe in self.pipes:
                pipe.draw(self.screen)

            # Draw score
            score_text = self.font.render(f"Score: {self.score}", True, BLACK)
            self.screen.blit(score_text, (10, 10))

        elif self.game_state == GAME_STATE_GAME_OVER:
            text = self.font.render(
                f"Game Over! Score: {self.score}", True, BLACK)
            self.screen.blit(
                text, (WINDOW_WIDTH//2 - text.get_width()//2, WINDOW_HEIGHT//2))
            restart_text = self.font.render(
                "Press SPACE to Restart", True, BLACK)
            self.screen.blit(restart_text, (WINDOW_WIDTH//2 -
                             restart_text.get_width()//2, WINDOW_HEIGHT//2 + 40))

        pygame.display.flip()

    def run(self):
        """Main game loop."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
