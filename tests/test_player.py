import unittest
from unittest.mock import patch, MagicMock
import pygame
from src.game import Player

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pygame.init()
        cls.screen = pygame.display.set_mode((1280, 720))


    @classmethod
    def tearDownClass(cls) -> None:
        pygame.quit()


    def setUp(self) -> None:
        self.player = Player(color=('lime'), starting_position=(640, 360))


    def tearDown(self) -> None:
        del self.player


    def test_player_initialization(self):
        # Test initial position and attributes
        self.assertEqual(self.player._position, pygame.Vector2(640, 360))
        self.assertEqual(self.player._color, ('lime'))
        self.assertEqual(self.player._size, 20.0)
        self.assertEqual(self.player._speed, 100.0)


    @patch('pygame.key.get_pressed')
    def test_player_movement(self, mock_get_pressed):
        # Mock the keys pressed
        mock_get_pressed.return_value = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: True}

        initial_position = self.player._position.xy
        self.player.process(1)  # Simulate 1 second of time passing

        # Check if player moved to the right
        self.assertEqual(self.player._position.x, initial_position[0] + 100.0)
        self.assertEqual(self.player._position.y, initial_position[1])


    def test_player_render(self):
        # Mock the screen and render the player
        self.player.render(self.screen)

        # No direct way to check rendering, but we can ensure no errors were raised
        self.assertTrue(True)