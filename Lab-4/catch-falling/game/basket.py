"""
Basket: the player-controlled catcher at the bottom of the screen.
"""

import pygame

BOOST_DURATION_FRAMES = 180
BOOST_MULTIPLIER = 2.0


class Basket:
    def __init__(self, x, y, width=90, height=24, speed=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.boosted_frames = 0
        self.normal_speed = speed
        self.boost_speed = speed * BOOST_MULTIPLIER

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

    @property
    def is_boosted(self):
        return self.boosted_frames > 0

    def activate_boost(self):
        if not self.is_boosted:
            self.boosted_frames = BOOST_DURATION_FRAMES
            self.speed = self.boost_speed

    def update_boost(self):
        if not self.is_boosted:
            return
        self.boosted_frames -= 1
        if self.boosted_frames == 0:
            self.speed = self.normal_speed
