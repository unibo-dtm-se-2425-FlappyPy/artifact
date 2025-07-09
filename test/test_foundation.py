import unittest
import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    BACKGROUND_COLOR,
)

class TestFoundation(unittest.TestCase):
    """Test cases for the foundation of the game"""

    def test_window_dimensions(self):
        """Test if the window dimensions are set correctly"""
        self.assertEqual(WINDOW_WIDTH, 400)
        self.assertEqual(WINDOW_HEIGHT, 600)

    def test_aspect_ratio(self):
        """Verify aspect ratio makes sense for a Flappy Bird game"""
        aspect_ratio = WINDOW_HEIGHT / WINDOW_WIDTH
        self.assertGreater(aspect_ratio, 1.0)

    def test_frame_rate_setting(self):
        """Test if the frame rate is to appropriate value"""
        self.assertEqual(FPS, 60)
        self.assertGreater(FPS, 30)
    
    def test_background_color(self):
        """Test if the background color is valid RGB tuple"""
        self.assertIsInstance(BACKGROUND_COLOR, tuple)
        self.assertEqual(len(BACKGROUND_COLOR), 3)
    
        for color_value in BACKGROUND_COLOR:
            self.assertGreaterEqual(color_value, 0)
            self.assertLessEqual(color_value, 255)
            self.assertIsInstance(color_value, int)
    
if __name__ == '__main__':
    unittest.main()
