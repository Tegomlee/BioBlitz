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
File: constants.py
Description: Defines a set of constants gor the game as enums
                due to their immutability
Author: Bryan Sanchez [Tegomlee]
Date: 08-05-2024
License: GPL v3.0

Dependencies:
- enum
"""

from enum import Enum

class Constants(Enum):
    # Window
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    # Map Size
    MAP_SIZE_X = 5000
    MAP_SIZE_Y = 5000

    # Player
    PLAYER_SIZE = 20.0
    PLAYER_SPEED = 300.0

    # Food
    FOOD_SIZE = 10.0
