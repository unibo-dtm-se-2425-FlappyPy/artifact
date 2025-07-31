import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

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
        self.assertEqual(
            rect.width, self.bird.width, "Rectangle width should match bird width"
        )
        self.assertEqual(
            rect.height, self.bird.height, "Rectangle height should match bird height"
        )

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

    def test_game_state_initialization(self):
        """Test that game starts in correct initial state"""
        # These would be tested in a game state manager, but we can test the concept
        bird = Bird()

        # Bird should start at initial position
        from FlappyPy.main import BIRD_START_X, BIRD_START_Y

        self.assertEqual(
            bird.x, BIRD_START_X, "Bird should start at initial x position"
        )
        self.assertEqual(
            bird.y, BIRD_START_Y, "Bird should start at initial y position"
        )
        self.assertEqual(bird.velocity, 0, "Bird should start with zero velocity")

    def test_bird_collision_triggers_game_over_condition(self):
        """Test that collision detection can trigger game over logic"""
        # Position bird to collide with pipe
        self.bird.x = self.pipe.x + 10
        self.bird.y = self.pipe.top_height - 10

        # Collision should be detected (this would trigger game over in main loop)
        collision_detected = self.bird.check_collision_with_pipe(self.pipe)
        self.assertTrue(
            collision_detected, "Collision should be detected for game over trigger"
        )

    def test_bird_reset_functionality(self):
        """Test that bird can be properly reset to initial state"""
        # Modify bird state (simulate gameplay)
        self.bird.x = 200
        self.bird.y = 400
        self.bird.velocity = 15

        # Reset bird to initial state (simulate restart)
        from FlappyPy.main import BIRD_START_X, BIRD_START_Y

        reset_bird = Bird()  # This simulates creating new bird on restart

        # Verify reset worked correctly
        self.assertEqual(
            reset_bird.x, BIRD_START_X, "Reset bird should be at initial x"
        )
        self.assertEqual(
            reset_bird.y, BIRD_START_Y, "Reset bird should be at initial y"
        )
        self.assertEqual(reset_bird.velocity, 0, "Reset bird should have zero velocity")

    def test_multiple_collision_scenarios(self):
        """Test collision detection across different pipe positions"""
        # Test with pipe at different gap heights
        high_pipe = Pipe(150, 100)  # High gap
        low_pipe = Pipe(200, WINDOW_HEIGHT - 100)  # Low gap

        # Bird should be able to fly through both gaps safely
        self.bird.x = 160
        self.bird.y = 90  # In high gap
        self.assertFalse(
            self.bird.check_collision_with_pipe(high_pipe),
            "Bird should fit through high gap",
        )

        self.bird.y = WINDOW_HEIGHT - 110  # In low gap
        self.assertFalse(
            self.bird.check_collision_with_pipe(low_pipe),
            "Bird should fit through low gap",
        )


if __name__ == "__main__":
    unittest.main()
