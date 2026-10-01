import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from game.collision import is_caught
from game.falling_object import FallingObject
from game.game_engine import GameEngine


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


if __name__ == "__main__":
    unittest.main()
