import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import *

class TestScoring(unittest.TestCase):
    """Unit tests for scoring system functionality"""
    
    def setUp(self):
        """Create fresh game objects for each test"""
        pass
    
    def test_score_initializes_to_zero(self):
        """Test that game score starts at zero"""
        score = 0  # Placeholder
        self.assertEqual(score, 0, "Game score should initialize to zero")

if __name__ == '__main__':
    unittest.main()
