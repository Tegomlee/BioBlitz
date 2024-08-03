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
File: collisions.py
Description: Defines the Collisions static class for the game.
             Handles all collsion based functionality.
Author: Tegomlee
Date: 08-01-2024
License: GPL v3.0

Dependencies:
- pygame

Modifications:
08-02-2024 (Tegomlee) - Made the class more generic.
                        Specifically meant to handle pygame Sprite()
"""

# Imports
import pygame

# Class that handles all collisions in the game
class Collisions:

    @staticmethod
    def check_for_collisions_between(main_object: pygame.sprite.Sprite, object_list: list[pygame.sprite.Sprite]) -> pygame.sprite.Sprite:
        # Iterate through each item in the list
        for object_in_list in object_list:
            if main_object.rect.colliderect(object_in_list.rect):
                return object_in_list
            
        return None
