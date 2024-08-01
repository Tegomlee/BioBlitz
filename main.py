import pygame

import random

from src.game import Player
from src.game import Food
from src.game import Collisions


# Random color for the player
def get_random_color():
    r = random.randint(0, 255) # red
    g = random.randint(0, 255) # green
    b = random.randint(0, 255) # blue

    return (r, g, b)


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

    # Initialize the player
    player_color = get_random_color()
    player = Player(color=player_color, starting_position=(640, 360))

    # Initialize the food list
    foods = []
    for i in range(0, 7):
        food = Food(get_random_color())
        food.randomize_position()
        foods.append(food)

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

        # Check for collisions
        check_collisions(player, foods)

        #DEBUGGING: Print the fps to the console
        fps = clock.get_fps()
        print(f'FPS: {fps:.2f}')

        # ------------------------------------------------------------------------

        # Render GameObjects -----------------------------------------------------
        screen.fill("grey58") # Clean the screen

        #TODO: Put game objects here for rendering
        player.render(screen)

        for food in foods:
            food.render(screen)

        pygame.display.flip() # Sends the final frame to the monitor

        # ------------------------------------------------------------------------


# Main entry point
if __name__ == '__main__':
    main()