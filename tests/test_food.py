import unittest
from unittest.mock import patch
import pygame
from src.game import Food

class TestFood(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pygame.init()
        cls.screen = pygame.display.set_mode((1280, 720))


    @classmethod
    def tearDownClass(cls) -> None:
        pygame.quit()


    def setUp(self) -> None:
        self.food = Food(color=('red'))

        self.food_list = [Food(color=('red')) for _ in range(5)]


    def tearDown(self) -> None:
        del self.food
        del self.food_list


    def test_food_initialization(self):
        # Test initial position and attributes
        self.assertEqual(self.food.rect.center, (0, 0))  # Since it's initially set to (0, 0)
        self.assertEqual(self.food.rect.size, (self.food._size * 2, self.food._size * 2))

    def test_food_list(self):
        # Check that the list contains the correct number of Food objects
        self.assertEqual(len(self.food_list), 5)

        # Ensure all items in the list are instances of Food and have a valid rect
        for food in self.food_list:
            self.assertIsInstance(food, Food)
            self.assertIsInstance(food.rect, pygame.Rect)


    def test_food_randomize_position(self):
        self.food.randomize_position()
        self.assertTrue(self.food.rect.centerx in range(-20, 21))
        self.assertTrue(self.food.rect.centery in range(-20, 21))
