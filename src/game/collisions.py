# Imports
import pygame

from src.game import Player
from src.game import Food

# Class that handles all collisions in the game
class Collisions:

    @staticmethod
    def check_for_collisions_between(player: Player, foods: list[Food]) -> Food:
        # Create the players bounding box
        player_rect = pygame.Rect(player.get_position().x - player.get_size(),
                                  player.get_position().y - player.get_size(),
                                  player.get_size(), player.get_size())
        
        # Create each food's bounding box
        for food in foods:
            food_rect = pygame.Rect(food.get_position().x - food.get_size(),
                                    food.get_position().y - food.get_size(),
                                    food.get_size(), food.get_size())
            if player_rect.colliderect(food_rect):
                return food
            
        return None # No collision
