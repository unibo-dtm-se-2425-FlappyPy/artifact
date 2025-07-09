import pygame
import sys

# Game constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue

def main():
    """Main game function - our game's entry point"""

    # Initialize Pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("FlappyPy")

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with the background color
        screen.fill(BACKGROUND_COLOR)

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
