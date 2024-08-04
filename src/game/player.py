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
File: player.py
Description: Defines the Player class for the game.
             Defines the player's logic in the process function
Author: Bryan Sanchez [Tegomlee]
Date: 07-31-2024
License: GPL v3.0

Dependencies:
- pygame

Modifications:
08-02-2024 (Tegomlee) - Removed the rendering logic and getters from the class.
                        Made the class inherit Sprite()

"""

import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, color: pygame.Color, starting_position) -> None:
        # Create the Sprite() super class
        super().__init__()

        # Initialize the plyer's member variables
        self._position = pygame.Vector2(starting_position)
        self._color = color
        self._size = 20.0
        self._speed = 300.0

        # Set up the player's sprite
        self.image = pygame.Surface((self._size * 2, self._size * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self._color, (self._size, self._size), self._size)
        self.rect = self.image.get_rect(center=self._position)


    # All the logical updates for the player
    def process(self, delta_time) -> None:
        keys = pygame.key.get_pressed() # Get the list of all the keys
        direction = pygame.Vector2(0, 0) # The Vector2 representation of the player's desired direction

        # Get the direction the player wants to go
        if keys[pygame.K_w]:
            direction.y -= 1.0
        if keys[pygame.K_s]:
            direction.y += 1.0
        if keys[pygame.K_a]:
            direction.x -= 1.0
        if keys[pygame.K_d]:
            direction.x += 1.0

        # Normalize the vector so diagonal movement is the same
        if not direction.magnitude() < 0.1:
            direction = direction.normalize()

        # Apply the normalized direction to the player's position
        self._position += direction * self._speed * delta_time

        # Apply the position to rect transform
        self.rect.center = self._position

        print(f"Player Position: {self._position}")
