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
File: camera.py
Description: Defines the Camera class for the game.
             Creates and manages a pygame Surface to render the game
Author: Tegomlee
Date: 08-02-2024
License: GPL v3.0

Dependencies:
- pygame

Modifications:
08-03-2024 (Tegomlee) - Added linear interpolation to the camera class to
                        allow for smoother camera movement and add more life
                        to the game.
"""

import pygame

class Camera:

    def __init__(self, width: int, height: int) -> None:
        self._camera = pygame.Rect(0, 0, width, height)
        self._width = width
        self._height = height
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._lerp_factor = 0.1


    # Adjust entity's position based on the camera's position and draw it
    def draw(self, entity: pygame.sprite.Sprite) -> None:
        adjusted_position = entity.rect.move(-self._camera.x, -self._camera.y)
        self._surface.blit(entity.image, adjusted_position)


    # Center the camera on the target (usually the player)
    def update(self, target: pygame.sprite.Sprite) -> None:
        target_x = target.rect.centerx - self._width // 2
        target_y = target.rect.centery - self._height // 2

        self._camera.x = self._lerp(self._camera.x, target_x, self._lerp_factor)
        self._camera.y = self._lerp(self._camera.y, target_y, self._lerp_factor)

        print(f"Camera Position: {self._camera.x}, {self._camera.y}")


    # Blit the camera's surface onto the main screen
    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self._surface, (0, 0))
        self._surface.fill((0, 0, 0, 0)) #Clear the surface for the next frame


    # Linear interpolation helper function
    def _lerp(self, start: float, end: float, factor: float) -> float:
        return start + (end - start) * factor
