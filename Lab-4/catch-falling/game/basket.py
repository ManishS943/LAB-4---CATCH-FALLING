"""
Basket: the player-controlled catcher at the bottom of the screen.
"""

import pygame


class Basket:
    def __init__(self, x, y, width=90, height=24, speed=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.boosted_frames = 0
        self.normal_speed = speed
        self.boost_speed = speed

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2), int(self.y - self.height / 2),
            self.width, self.height,
        )

    def move(self, direction, screen_width):
        """Move continuously while a direction key is held and stay on-screen."""
        self.x += direction * self.speed
        half_width = self.width / 2
        self.x = max(half_width, min(screen_width - half_width, self.x))
