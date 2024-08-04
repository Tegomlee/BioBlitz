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
File: color_helper.py
Description: Definition for the ColorHelper() class, this class will basically
             randomize the colors of entities. It's sole purpose is to clear some
             of main.py
Author: Bryan Sanchez [Tegomlee]
Date: 08-03-2024
License: GPL v3.0

Dependencies:
- pygame
- random
"""

import pygame

import random

class ColorHelper:

    # Generates a random color by randomizing the {R, G, B} values
    @staticmethod
    def get_random_color() -> pygame.Color:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        color = pygame.Color(r, g, b)

        return color
    