import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import Bird, Pipe, WINDOW_HEIGHT, PIPE_GAP

class TestCollisionDetection(unittest.TestCase):
    """Unit tests for collision detection and game mechanics"""
    
    def setUp(self):
        """Create fresh instances for each test"""
        self.bird = Bird()
        self.pipe = Pipe(100, WINDOW_HEIGHT // 2)
    
    def test_bird_get_rect(self):
        """Test that bird creates correct collision rectangle"""
        rect = self.bird.get_rect()
        
        self.assertEqual(rect.x, self.bird.x, "Rectangle x should match bird x")
        self.assertEqual(rect.y, self.bird.y, "Rectangle y should match bird y")
        self.assertEqual(rect.width, self.bird.width, "Rectangle width should match bird width")
        self.assertEqual(rect.height, self.bird.height, "Rectangle height should match bird height")
    
    def test_no_collision_in_gap(self):
        """Test that bird flying through gap doesn't trigger collision"""
        # Position bird safely in the middle of the gap
        gap_center = self.pipe.gap_center_y
        self.bird.x = self.pipe.x + 10  # Bird overlapping pipe horizontally
        self.bird.y = gap_center - (self.bird.height // 2)  # Bird centered in gap
        
        # Should not detect collision
        collision = self.bird.check_collision_with_pipe(self.pipe)
        self.assertFalse(collision, "Bird in gap should not collide with pipe")
    
    def test_collision_with_top_pipe(self):
        """Test collision detection with top pipe"""
        # Position bird to hit top pipe
        self.bird.x = self.pipe.x + 10  # Overlapping horizontally
        self.bird.y = self.pipe.top_height - 10  # Overlapping top pipe
        
        # Should detect collision
        collision = self.bird.check_collision_with_pipe(self.pipe)
        self.assertTrue(collision, "Bird should collide with top pipe")
    
    def test_collision_with_bottom_pipe(self):
        """Test collision detection with bottom pipe"""
        # Position bird to hit bottom pipe
        self.bird.x = self.pipe.x + 10  # Overlapping horizontally
        self.bird.y = self.pipe.bottom_y + 10  # Overlapping bottom pipe
        
        # Should detect collision
        collision = self.bird.check_collision_with_pipe(self.pipe)
        self.assertTrue(collision, "Bird should collide with bottom pipe")
    
    def test_no_collision_when_not_overlapping(self):
        """Test that bird not overlapping pipe doesn't trigger collision"""
        # Position bird completely away from pipe
        self.bird.x = self.pipe.x + self.pipe.width + 50  # Past the pipe
        self.bird.y = WINDOW_HEIGHT // 2  # Anywhere vertically
        
        # Should not detect collision
        collision = self.bird.check_collision_with_pipe(self.pipe)
        self.assertFalse(collision, "Bird not overlapping pipe should not collide")

if __name__ == '__main__':
    unittest.main()
