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
File: main.py
Description: The main entry point of the program.
Author: Bryan Sanchez [Tegomlee]
Date: 07-31-2024
License: GPL v3.0

Dependencies:
- pygame
- random

Modifications:
08-01-2024 (Tegomlee) - Removed references to the Engine class since it
                            would no longer be part of the code base.
                        Added Food references to the game since the main
                            method will now handle the game logic under the hood.

08-02-2024 (Tegomlee) - Added the Camera references to the main entry point to
                            handle rendering of the game.
"""

import pygame

from src.game import Player
from src.game import Food

from src.framework import Camera
from src.framework import Collisions
from src.framework import ColorHelper


# Calls the static method for rchecking collisions
def check_collisions(player: Player, foods: list[Food]):
    food = Collisions.check_for_collisions_between(player, foods)

    if food is not None:
        food.randomize_position()


# Main function
def main() -> None:

    # Initialize the pygame API
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock() # used for deltaTime
    running = True
    font = pygame.font.SysFont(None, 30) # used for drawing info to the screen

    # Initialize the player
    player_color = ColorHelper.get_random_color()
    player = Player(color=player_color, starting_position=(640, 360))

    # Initialize the food list
    food_list = []
    for i in range(0, 7):
        food = Food(ColorHelper.get_random_color())
        food.randomize_position()
        food_list.append(food)

    foods = tuple(food_list)

    # Initialize the camera
    camera = Camera(1280, 720)

    # Main game loop
    while running:
        
        # Event Handling ---------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the 'x' button is pressed
                running = False

        # ------------------------------------------------------------------------
        
        # Process GameObjects ----------------------------------------------------
        delta_time = clock.tick(60) / 1000 # Used for frame rate independence

        #TODO: Put game objects here for updating
        player.process(delta_time)

        camera.update(player)

        # Check for collisions
        check_collisions(player, foods)

        # Get the FPS
        fps = clock.get_fps()

        # ------------------------------------------------------------------------

        # Render GameObjects -----------------------------------------------------
        screen.fill("grey58") # Clean the screen

        # Draw the game objects to the camera's surface
        camera.draw(player)

        for food in foods:
            camera.draw(food)

        # Sends the camera's surface to the screen
        camera.render(screen) 

        # Render the FPS text
        fps_text = font.render(f"FPS: {int(fps)}", True, pygame.Color('white'))
        screen.blit(fps_text, (10, 10))

        # Sends the final frame to the monitor
        pygame.display.flip()

        # ------------------------------------------------------------------------


# Main entry point
if __name__ == '__main__':
    main()