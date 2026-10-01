import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from game.collision import is_caught
from game.falling_object import FallingObject
from game.game_engine import GameEngine
from game.renderer import WIDTH


class CollisionTests(unittest.TestCase):
    def test_object_above_basket_is_not_caught(self):
        engine = GameEngine()
        obj = FallingObject(x=engine.basket.x, y=10)

        self.assertFalse(is_caught(engine.basket.get_rect(), obj))

    def test_object_overlapping_basket_is_caught(self):
        engine = GameEngine()
        obj = FallingObject(x=engine.basket.x, y=engine.basket.y)

        self.assertTrue(is_caught(engine.basket.get_rect(), obj))

    def test_two_adjacent_objects_are_both_scored(self):
        engine = GameEngine()
        engine.frames_until_spawn = 999
        engine.objects = [
            FallingObject(x=engine.basket.x - 10, y=engine.basket.y, speed=0),
            FallingObject(x=engine.basket.x + 10, y=engine.basket.y, speed=0),
        ]

        engine.update()

        self.assertEqual(engine.score, 2)
        self.assertEqual(engine.objects, [])


class BasketMovementTests(unittest.TestCase):
    def test_left_boundary_keeps_entire_basket_on_screen(self):
        engine = GameEngine()
        engine.basket.x = 0

        engine.basket.move(-1, WIDTH)

        self.assertEqual(engine.basket.get_rect().left, 0)

    def test_right_boundary_keeps_entire_basket_on_screen(self):
        engine = GameEngine()
        engine.basket.x = WIDTH

        engine.basket.move(1, WIDTH)

        self.assertEqual(engine.basket.get_rect().right, WIDTH)

    def test_held_direction_moves_once_per_frame(self):
        engine = GameEngine()
        starting_x = engine.basket.x

        for _ in range(10):
            engine.basket.move(1, WIDTH)

        self.assertEqual(engine.basket.x, starting_x + 10 * engine.basket.speed)


if __name__ == "__main__":
    unittest.main()
