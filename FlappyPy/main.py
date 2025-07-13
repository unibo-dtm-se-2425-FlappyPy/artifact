import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

import pygame
import sys

# Game constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue

# Bird constants
BIRD_WIDTH = 30
BIRD_HEIGHT = 30
BIRD_COLOR = (255, 255, 0)  # Yellow
BIRD_START_X = 50
BIRD_START_Y = WINDOW_HEIGHT // 2

# Bird class
class Bird:
    """Class representing the bird in the game"""

    def __init__(self):
        self.x = BIRD_START_X
        self.y = BIRD_START_Y
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.velocity = 0
        self.gravity = 0.5
    
    def update(self):
        """Update the bird's position based on physics"""
        self.velocity += self.gravity
        self.y += self.velocity
        self.check_boundaries()
    
    def check_boundaries(self):
        """Prevent the bird from flying off screen edges"""
        # Top boundary
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        
        # Bottom boundary
        if self.y + self.height > WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - self.height
            self.velocity = 0
    
    def draw(self, screen):
        """Draw the bird on the screen"""
        pygame.draw.rect(screen, BIRD_COLOR, (self.x, self.y, self.width, self.height))
    
    def jump(self):
        """Make the bird jump up"""
        self.velocity = -8

def main():
    """Main game function - our game's entry point"""

    # Initialize Pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("FlappyPy")

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Create the bird
    bird = Bird()

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        
        # Update game physics
        bird.update()
        
        # Fill the screen with the background color
        screen.fill(BACKGROUND_COLOR)

        # Draw the bird
        bird.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)
    
    # Clean shutdown
    pygame.quit()
    sys.exit()

# Entry point for the game - "if this file is being run directly!"
if __name__ == "__main__":
    main()
