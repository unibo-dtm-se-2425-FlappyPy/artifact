import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import Score

class TestScoreDisplay(unittest.TestCase):
    """Unit tests for score display functionality"""
    
    def setUp(self):
        """Create fresh score object for each test"""
        self.score = Score()
    
    def test_score_text_formatting(self):
        """Test that score formats correctly for display"""
        expected_text = "Score: 0"
        actual_text = f"Score: {self.score.get_current_score()}"
        self.assertEqual(actual_text, expected_text, "Initial score should format as 'Score: 0'")
    
    def test_score_text_after_increment(self):
        """Test that score formats correctly after incrementing"""
        self.score.add_point()
        expected_text = "Score: 1"
        actual_text = f"Score: {self.score.get_current_score()}"
        self.assertEqual(actual_text, expected_text, "Score should format as 'Score: 1' after one point")

if __name__ == '__main__':
    unittest.main()
