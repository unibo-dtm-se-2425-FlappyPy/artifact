import unittest
import sys
import os
import pygame

# Add the FlappyPy package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from FlappyPy.main import show_game_over_screen, Score, WINDOW_WIDTH, WINDOW_HEIGHT

class TestGameOverDisplay(unittest.TestCase):
    """Unit tests for game over display functionality"""
    
    def setUp(self):
        """Set up pygame and test objects for each test"""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font(None, 36)
        self.score = Score()
        # Add some points to test score display
        self.score.add_point()
        self.score.add_point()
        self.score.add_point()
    
    def tearDown(self):
        """Clean up pygame after each test"""
        pygame.quit()
    
    def test_game_over_screen_function_exists(self):
        """Test that show_game_over_screen function can be called"""
        try:
            show_game_over_screen(self.screen, self.font, self.score)
        except Exception as e:
            self.fail(f"show_game_over_screen() raised an exception: {e}")
    
    def test_game_over_screen_displays(self):
        """Test that game over screen function executes without errors"""
        try:
            show_game_over_screen(self.screen, self.font, self.score)
            success = True
        except Exception as e:
            success = False
        
        self.assertTrue(success, "Game over screen should display without errors")

    def test_game_over_screen_with_different_scores(self):
        """Test game over screen with various score values"""
        # Score values to test
        test_scores = [0, 1, 5, 10, 99, 100, 999, 1000, 10000]
        
        for score_value in test_scores:
            test_score = Score()
            for _ in range(score_value):
                test_score.add_point()
            
            try:
                show_game_over_screen(self.screen, self.font, test_score)
                success = True
            except Exception:
                success = False
            
            self.assertTrue(success, f"Game over screen should work with score {score_value}")

if __name__ == '__main__':
    unittest.main()
