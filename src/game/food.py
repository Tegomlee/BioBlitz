"""
    BioBlitz is an Agar.io clone in python I wrote for Educational purposes
    Copyright (C) 2024  Bryan Sanchez

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

"""
File: food.py
Description: Defines the Food class for the game.
             Defines the food's randomization of position
               for reusing of resources
Author: Bryan Sanchez [Tegomlee]
Date: 07-31-2024
License: GPL v3.0

Dependencies:
- pygame
- random

Modifications:
08-02-2024 (Tegomlee) - Removed the rendering logic and getters from the class.
                        Made the class inherit Sprite()

08-05-2024 (Tegomlee) - Implemented the constants enums to the food class.
"""

import pygame

import random

from .constants import Constants

class Food(pygame.sprite.Sprite):

    def __init__(self, color):
        # Super class initialization: Sprite()
        super().__init__()

        # Member variable initialization
        self._color = color
        self._position = pygame.Vector2(0, 0)
        self._size = Constants.FOOD_SIZE.value

        # Set the food's sprite
        self.image = pygame.Surface((self._size * 2, self._size * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self._color, (self._size, self._size), self._size)
        self.rect = self.image.get_rect(center=self._position)


    def randomize_position(self):
        x = random.randrange(-20, 20)
        y = random.randrange(-20, 20)

        self._position = pygame.Vector2(x, y)
        self.rect.center = self._position
