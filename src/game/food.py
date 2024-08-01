import pygame

import random

class Food:

    def __init__(self, color):
        self._color = color
        self._position = pygame.Vector2(0, 0)
        self._size = 10.0


    def randomize_position(self):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)

        self._position = pygame.Vector2(x, y)


    def render(self, screen):
        pygame.draw.circle(screen, self._color, self._position, self._size)

        