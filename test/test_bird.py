import unittest
import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import Bird, BIRD_START_X, BIRD_START_Y, BIRD_WIDTH, BIRD_HEIGHT

class TestBird(unittest.TestCase):
    """Unit tests for the Bird class"""

    def setUp(self):
        """Create a fresh Bird instance for each test"""
        self.bird = Bird()
    
    def test_bird_initialiazation(self):
        """Test that the bird is initialized with correct attributes"""
        self.assertEqual(self.bird.x, BIRD_START_X)
        self.assertEqual(self.bird.y, BIRD_START_Y)
        self.assertEqual(self.bird.width, BIRD_WIDTH)
        self.assertEqual(self.bird.height, BIRD_HEIGHT)
    
    def test_bird_jump(self):
        """Test that the bird jumps correctly"""
        initial_y = self.bird.y
        self.bird.jump()
        
        self.assertEqual(self.bird.velocity, -8, "Jump should set velocity to -8")
        self.assertEqual(self.bird.y, initial_y, "Bird's y position should not change until next update()")
        
        self.bird.update()
        self.assertLess(self.bird.y, initial_y, "Bird should move up after jump and update")
    
    def test_multiple_jumps(self):
        """Test that multiple jumps work correctly"""
        initial_y = self.bird.y
        
        # Multiple jumps should reset velocity each time
        self.bird.jump()
        self.assertEqual(self.bird.velocity, -8, "First jump should set velocity to -8")
        
        self.bird.jump()
        self.assertEqual(self.bird.velocity, -8, "Socond jump should reset velocity to -8")
        
        self.bird.jump()
        self.assertEqual(self.bird.velocity, -8, "Third jump should reset velocity to -8")

        # Psition should still be unchanged until next update
        self.assertEqual(self.bird.y, initial_y, "Bird's y position should not change until next update()")
        
        
        self.bird.update()
        self.assertLess(self.bird.y, initial_y, "Bird should move up after jump and update()")
    
    def test_bird_position_bounds(self):
        """Test bird positioning relative to screen"""
        self.assertGreaterEqual(self.bird.x, 0, "Bird's x position should not be negative")
        self.assertGreaterEqual(self.bird.y, 0, "Bird's y position should not be negative")
        self.assertLessEqual(self.bird.x, 400, "Bird's x position should not exceed window width")
        self.assertLessEqual(self.bird.y, 600, "Bird's y position should not exceed window height")

if __name__ == '__main__':
    unittest.main()
        