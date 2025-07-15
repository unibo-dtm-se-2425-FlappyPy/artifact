import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import *

class TestScoring(unittest.TestCase):
    """Unit tests for scoring system functionality"""
    
    def setUp(self):
        """Create fresh scoring objects for each test"""
        pass
    
    def test_score_class_initialization(self):
        """Test that Score class initializes with zero points"""
        score = Score()
        self.assertEqual(score.get_current_score(), 0, 
                        "Score should initialize to zero")
        
    def test_score_increment(self):
        """Test that score can be incremented by one point"""
        score = Score()
        score.add_point()
        self.assertEqual(score.get_current_score(), 1,
                        "Score should increment to 1 after adding point")

if __name__ == '__main__':
    unittest.main()
