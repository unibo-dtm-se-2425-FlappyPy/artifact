import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

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
        self.assertEqual(
            actual_text, expected_text, "Initial score should format as 'Score: 0'"
        )

    def test_score_text_after_increment(self):
        """Test that score formats correctly after incrementing"""
        self.score.add_point()
        expected_text = "Score: 1"
        actual_text = f"Score: {self.score.get_current_score()}"
        self.assertEqual(
            actual_text,
            expected_text,
            "Score should format as 'Score: 1' after one point",
        )

    def test_font_render_creates_valid_surface(self):
        """Test that font.render() creates a Surface with valid properties"""
        import pygame

        pygame.init()

        font = pygame.font.Font(None, 36)

        text_surface = font.render("Score: 5", True, (255, 255, 255))

        self.assertIsNotNone(text_surface, "font.render() should return a Surface")

        self.assertTrue(
            hasattr(text_surface, "get_width"), "Surface should have get_width() method"
        )
        self.assertTrue(
            hasattr(text_surface, "get_height"),
            "Surface should have get_height() method",
        )

        self.assertGreater(
            text_surface.get_width(), 0, "Text surface should have positive width"
        )
        self.assertGreater(
            text_surface.get_height(), 0, "Text surface should have positive height"
        )

        pygame.quit()


if __name__ == "__main__":
    unittest.main()
