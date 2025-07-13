import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import Bird, WINDOW_HEIGHT

class testBoundaryChecking(unittest.TestCase):
    """Unit tests for boundary checking behavior"""
    
    def setUp(self):
        self.bird = Bird()
    
    def test_top_boundary_collision(self):
        """Test that the bird stops at the top screen boundary"""
        # Position the bird near the top and give it an upward velocity
        self.bird.y = 5
        self.bird.velocity = -10
        
        self.bird.update()
        
        self.assertEqual(self.bird.y, 0, "Bird should be clamped to the top boundary")
        self.assertEqual(self.bird.velocity, 0, "Bird's velocity should be reset to 0 at the top boundary")
    
    def test_bottom_boundary_collision(self):
        """Test that the bird stops at the bottom screen boundary"""
        # Position the bird near the bottom and give it a downward velocity
        self.bird.y = WINDOW_HEIGHT - self.bird.height - 5
        self.bird.velocity = 10
        
        self.bird.update()
        
        expected_y = WINDOW_HEIGHT - self.bird.height
        self.assertEqual(self.bird.y, expected_y, "Bird should be clamped to the bottom boundary")
        self.assertEqual(self.bird.velocity, 0, "Bird's velocity should be reset to 0 at the bottom boundary")
    
    def test_no_boundary_collision_in_middle(self):
        """Test that the bird can move normally when not hitting boundaries"""
        # Position the bird in the middle of the screen
        self.bird.y = WINDOW_HEIGHT // 2
        self.bird.velocity = 3
        initial_y = self.bird.y
        
        self.bird.update()
        
        expexted_y = initial_y + (3 + self.bird.gravity)
        self.assertEqual(self.bird.y, expexted_y, "Bird should move normally in the middle area")
        self.assertNotEqual(self.bird.velocity, 0, "Bird's velocity should not be reset when not hitting boundaries")
    
    def test_multiple_top_boundary_hits(self):
        """Test that multiple consecutive hits at the top boundary"""
        
        self.bird.y = 0
        self.bird.velocity = -5
        
        self.bird.update()
        self.assertEqual(self.bird.y, 0, "Bird should be clamped to the top boundary on first hit")
        self.assertEqual(self.bird.velocity, 0, "Velocity should be reset to 0 on first hit")
        
        self.bird.update()
        self.assertEqual(self.bird.velocity, self.bird.gravity, "Gravity should affect velocity")
        self.assertEqual(self.bird.y, self.bird.gravity, "Bird should start falling due to gravity")
        
        self.assertGreater(self.bird.y, 0, "Bird should fall away from the top boundary")
    
    def test_boundary_with_jump(self):
        """Test that jumping works correctly near boundaries"""
        
        self.bird.y = 0
        self.bird.velocity = 0
        
        self.bird.jump()
        self.assertEqual(self.bird.velocity, -8, "Jump should set velocity even at boundary")
        
        self.bird.update()
        self.assertEqual(self.bird.y, 0, "Bird should stay at the top boundary after jump")
        self.assertEqual(self.bird.velocity, 0, "Velocity should reset to 0 after hitting the boundary")
    
    def test_gravity_still_works_within_bounds(self):
        """Test that gravity continues to work within screen boundaries"""
        
        self.bird.y = 100
        self.bird.velocity = 0
        
        for _ in range(5):
            self.bird.update()
        
        self.assertGreater(self.bird.y, 100, "Bird should fall due to gravity")
        self.assertGreater(self.bird.velocity, 0, "Bird should have downward velocity")
    
    def test_high_velocity_boundary_impact(self):
        """Test that boundary collisions with high velocity"""
        
        self.bird.y = 50
        self.bird.velocity = -100  # High upward velocity
        
        self.bird.update()
        
        self.assertEqual(self.bird.y, 0, "Bird should be clamped despite high velocity")
        self.assertEqual(self.bird.velocity, 0, "Velocity should be reset to 0 despite high value")
    
if __name__ == '__main__':
    unittest.main()
