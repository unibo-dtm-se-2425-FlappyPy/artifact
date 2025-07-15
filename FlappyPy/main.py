import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

import random
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

# Pipe constants
PIPE_WIDTH = 70
PIPE_COLOR = (0, 128, 0)  # Green
PIPE_GAP = 150  # Gap between top and bottom pipes
PIPE_X_START = WINDOW_WIDTH  # Start just off-screen right

# Pipe generation
PIPE_SPAWN_INTERVAL = 120 # Frames between pipe spawns (~2s at 60 FPS)
SAFE_MARGIN = 80 # Keeps gaps fully within the screen

# Score class
class Score:
    """Manages the player's score"""
    
    def __init__(self):
        """Initialize score to zero"""
        self.current_score = 0
    
    def get_current_score(self):
        """Return the current score value"""
        return self.current_score
    
    def add_point(self):
        """Increment the score by one point"""
        self.current_score += 1
    
# Pipe class
class Pipe:
    """Class representing pipes as obstacles in the game"""
    
    def __init__(self, x, gap_center_y):
        self.x = x
        self.width = PIPE_WIDTH
        self.gap_center_y = gap_center_y
        self.gap_size = PIPE_GAP
        self.speed = 3  # Pixels per frame
        
        # Calculate pipe hights
        self.top_height = gap_center_y - (self.gap_size // 2)
        self.bottom_y = gap_center_y + (self.gap_size // 2)
        self.bottom_height = WINDOW_HEIGHT - self.bottom_y
    
    def update(self):
        """Move pipe from right to left"""
        self.x -= self.speed
    
    def draw(self, screen):
        """Draw both top and bottom pipes"""
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, self.width, self.top_height))  # Top pipe
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.bottom_y, self.width, self.bottom_height))  # Bottom pipe

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
    
    def draw(self, screen):
        """Draw the bird on the screen"""
        pygame.draw.rect(screen, BIRD_COLOR, (self.x, self.y, self.width, self.height))
    
    def jump(self):
        """Make the bird jump up"""
        self.velocity = -8
    
    def get_rect(self):
        """Get bird's collision rectangle for collision detection"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def check_collision_with_pipe(self, pipe):
        """Check if the bird collides with a pipe"""
        bird_rect = self.get_rect()
        
        top_pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.top_height)
        if bird_rect.colliderect(top_pipe_rect):
            return True
        
        bottom_pipe_rect = pygame.Rect(pipe.x, pipe.bottom_y, pipe.width, pipe.bottom_height)
        if bird_rect.colliderect(bottom_pipe_rect):
            return True
        
        return False
    
    def check_collision_with_ground(self):
        """Check if bird has hit the bottom boundary (ground)"""
        return self.y + self.height >= WINDOW_HEIGHT

    def check_collision_with_ceiling(self):
        """Check if bird has hit the top boundary (ceiling)"""
        return self.y <= 0

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
    
    # Create initial pipes list
    pipes = []
    
    # Create scoring system
    score = Score()
    
    # Initialize game state
    game_over = False
    
    # Frame counter for pipe spawning
    frames_since_spawn = 0

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        # Reset the game
                        game_over = False
                        bird = Bird()
                        pipes = []
                        frames_since_spawn = 0
                    else:
                        bird.jump()
        
        # Update game
        if not game_over:
            
            bird.update()
            
            # Update the pipes movement
            for pipe in pipes:
                pipe.update()
            
            # Check pipe collisions
            for pipe in pipes:
                # Check if bird collides with this pipe
                if bird.check_collision_with_pipe(pipe):
                    game_over = True
                    print("GAME OVER! Press SPACE to play again.")
                
                # Check if bird has passed through this pipe
                if bird.x > pipe.x + pipe.width:
                    score.add_point()
                    print(f"Score: {score.get_current_score()}")
            
            # Check ground collision
            if bird.check_collision_with_ground():
                game_over = True
                print("GAME OVER! Press SPACE to play again.")
            
            # Remove off-screen pipes
            pipes = [p for p in pipes if p.x + p.width > 0]
            
            # Fill the screen with the background color
            screen.fill(BACKGROUND_COLOR)
            
            # Pipe spawning logic
            frames_since_spawn += 1
            if frames_since_spawn >= PIPE_SPAWN_INTERVAL:
                frames_since_spawn = 0
                
                gap_center = random.randint(
                    SAFE_MARGIN + PIPE_GAP // 2,
                    WINDOW_HEIGHT - SAFE_MARGIN - PIPE_GAP // 2
                )
                pipes.append(Pipe(PIPE_X_START, gap_center))
            
            # Draw the pipes
            for pipe in pipes:
                pipe.draw(screen)

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
