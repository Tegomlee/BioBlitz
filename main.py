import pygame

import random

from src.game import Player


# Random color for the player
def get_random_color():
    r = random.randint(0, 255) # red
    g = random.randint(0, 255) # green
    b = random.randint(0, 255) # blue

    return (r, g, b)


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

    # Main game loop
    while running:
        
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the 'x' button is pressed
                running = False
        
        # Process GameObjects
        delta_time = clock.tick(60) / 1000 # Used for frame rate independence

        #TODO: Put game objects here for updating
        player.process(delta_time)

        #DEBUGGING: Print the fps to the console
        fps = clock.get_fps()
        print(f'FPS: {fps:.2f}')

        # Render GameObjects
        screen.fill("grey58") # Clean the screen

        #TODO: Put game objects here for rendering
        player.render(screen)

        pygame.display.flip() # Sends the final frame to the monitor


# Main entry point
if __name__ == '__main__':
    main()