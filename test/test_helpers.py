import pygame

def create_mock_surface(width=32, height=32):
    """Create a mock surface for testing"""
    surface = pygame.Surface((width, height))
    surface.fill((255, 255, 0))  # Yellow rectangle
    return surface

def setup_test_environment():
    """Initialize pygame for testing"""
    pygame.init()
    pygame.display.set_mode((100, 100))
    return True
