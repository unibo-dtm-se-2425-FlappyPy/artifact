import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import (
    Pipe, PIPE_WIDTH, PIPE_COLOR, PIPE_GAP, 
    WINDOW_WIDTH, WINDOW_HEIGHT
)

class TestPipe(unittest.TestCase):
    """Unit tests for Pipe class functionality"""
    
    def setUp(self):
        """Create a fresh pipe instance for each test"""
        
        self.test_gap_center = WINDOW_HEIGHT // 2
        self.pipe = Pipe(100, self.test_gap_center)
    
    def test_pipe_initialization(self):
        """Test that pipe initializes with correct values"""
        
        self.assertEqual(self.pipe.x, 100, "Pipe should initialize at correct x position")
        self.assertEqual(self.pipe.width, PIPE_WIDTH, "Pipe should have correct width")
        self.assertEqual(self.pipe.gap_center_y, self.test_gap_center, "Pipe should store gap center")
        self.assertEqual(self.pipe.gap_size, PIPE_GAP, "Pipe should have correct gap size")
        self.assertEqual(self.pipe.speed, 3, "Pipe should have default speed")
    
    def test_pipe_gap_calculations(self):
        """Test that pipe calculates top and bottom heights correctly"""
        
        expected_top_height = self.test_gap_center - (PIPE_GAP // 2)
        expected_bottom_y = self.test_gap_center + (PIPE_GAP // 2)
        expected_bottom_height = WINDOW_HEIGHT - expected_bottom_y
        
        self.assertEqual(self.pipe.top_height, expected_top_height, 
                        "Top pipe height should be calculated correctly")
        self.assertEqual(self.pipe.bottom_y, expected_bottom_y, 
                        "Bottom pipe Y position should be calculated correctly")
        self.assertEqual(self.pipe.bottom_height, expected_bottom_height, 
                        "Bottom pipe height should be calculated correctly")
    
    def test_pipe_movement(self):
        """Test that pipe moves correctly when updated"""
        
        initial_x = self.pipe.x
        
        # Update once
        self.pipe.update()
        
        expected_x = initial_x - self.pipe.speed
        self.assertEqual(self.pipe.x, expected_x, "Pipe should move left by speed amount")
    
    def test_multiple_updates(self):
        """Test pipe movement over multiple frames"""
        
        initial_x = self.pipe.x
        
        # Update 5 times
        for _ in range(5):
            self.pipe.update()
        
        expected_x = initial_x - (self.pipe.speed * 5)
        self.assertEqual(self.pipe.x, expected_x, "Pipe should move correctly over multiple updates")
    
    def test_gap_size_consistency(self):
        """Test that gap between pipes is always correct size"""
        
        gap_actual_size = self.pipe.bottom_y - self.pipe.top_height
        self.assertEqual(gap_actual_size, PIPE_GAP, "Actual gap should match PIPE_GAP constant")
    
    def test_different_gap_positions(self):
        """Test pipes with different gap center positions"""
        
        # Test high gap
        high_pipe = Pipe(50, 100)
        self.assertEqual(high_pipe.gap_center_y, 100)
        self.assertGreater(high_pipe.bottom_height, high_pipe.top_height, "High gap should create taller bottom pipe")
        
        # Test low gap  
        low_pipe = Pipe(50, WINDOW_HEIGHT - 100)
        self.assertEqual(low_pipe.gap_center_y, WINDOW_HEIGHT - 100)
        self.assertGreater(low_pipe.top_height, low_pipe.bottom_height, "Low gap should create taller top pipe")
    
    def test_pipe_boundaries(self):
        """Test that pipe dimensions stay within reasonable bounds"""
        
        # Test that pipe heights are positive
        self.assertGreaterEqual(self.pipe.top_height, 0, 
                               "Top pipe height should be non-negative")
        self.assertGreaterEqual(self.pipe.bottom_height, 0, "Bottom pipe height should be non-negative")
        
        # Test that pipes don't exceed screen bounds
        self.assertLessEqual(self.pipe.top_height, WINDOW_HEIGHT, "Top pipe shouldn't exceed screen height")
        self.assertLessEqual(self.pipe.bottom_y + self.pipe.bottom_height, WINDOW_HEIGHT, "Bottom pipe shouldn't exceed screen height")

if __name__ == '__main__':
    unittest.main()
