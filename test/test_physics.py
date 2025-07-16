import unittest
import sys
import os
import pygame

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import Bird, BIRD_START_X, BIRD_START_Y

class TestPhysics(unittest.TestCase):
    """Unit tests for physics behavior"""
    
    def setUp(self):
        """Create a fresh bird instance for each test"""
        pygame.init()
        pygame.display.set_mode((1, 1))
        self.bird = Bird()
    
    def test_bird_has_physics_attributes(self):
        """Test that bird initializes with physics attributes"""
        self.assertEqual(self.bird.velocity, 0, "Bird should start with zero velocity")
        self.assertEqual(self.bird.gravity, 0.5, "Bird should have a correct gravity value")
    
    def test_gravity_affects_velocity(self):
        """Test that gravity increases velocity over time"""
        initial_velocity = self.bird.velocity
        
        self.bird.update()
        expected_velocity = initial_velocity + self.bird.gravity
        self.assertEqual(self.bird.velocity, expected_velocity, "Gravity should increase velocity by gravity amount")
    
    def test_velocity_affects_position(self):
        """Test that velocity changes bird's position"""
        initial_y = self.bird.y
        initial_velocity = 5.0  # Set a specific velocity to test
        
        self.bird.velocity = initial_velocity
        self.bird.update()
        
        expected_velocity_after_gravity = initial_velocity + self.bird.gravity
        expected_y = initial_y + expected_velocity_after_gravity
        
        self.assertEqual(self.bird.y, expected_y, "Position should change by velocity AFTER gravity is applied")
    
    def test_multiple_updates_accerlate_falling(self):
        """Test that multiple updates create accelerating fall"""
        initial_y = self.bird.y
        
        # Update multiple times
        self.bird.update() # velocity becomes 0.5, y increases by 0.5
        self.bird.update() # velocity becomes 1.0, y increases by 1.0
        self.bird.update() # velocity becomes 1.5, y increases by 1.5
        
        expected_y = initial_y + 0.5 + 1.0 + 1.5
        self.assertEqual(self.bird.y, expected_y, "Multiple updates should create accelerating fall")
    
    def test_jump_sets_upward_velocity(self):
        """Test that jumping sets velocity to upward value"""
        self.bird.velocity = 5 # Let the bird fall first
        
        self.bird.jump()
        expected_velocity = -8
        self.assertEqual(self.bird.velocity, expected_velocity, "Jump should set velocity to expected velocity")
    
    def test_jump_after_falling(self):
        """Test complete jump cycle after falling"""
        initial_y = self.bird.y
        
        self.bird.update()
        self.bird.update()
        fallen_y = self.bird.y
        
        self.bird.jump()
        self.bird.update()
        
        self.assertLess(self.bird.y, fallen_y, "Jump should move bird higher than fallen position")
    
    def test_physics_cycle_complete(self):
        """Test complete physics cycle: fall, jump, and fall again"""
        initial_y = self.bird.y
        
        # Fall
        self.bird.update()
        self.bird.update()
        
        # Jump
        self.bird.jump()
        
        # Move up
        self.bird.update()
        after_jump_y = self.bird.y
        
        # Should be moving up
        self.assertLess(after_jump_y, initial_y, "After jump, bird should be higher than start")
        
        # Continue falling
        for _ in range(30):
            self.bird.update()
        
        self.assertGreater(self.bird.y, initial_y, "Eventually gravity should overcome jump")

if __name__ == '__main__':
    unittest.main()
