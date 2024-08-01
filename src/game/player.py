import pygame

class Player:

    def __init__(self, color, starting_position) -> None:
        self._position = pygame.Vector2(starting_position)
        self._color = color
        self._size = 20.0
        self._speed = 300.0


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

    
    # The rendering happens here
    def render(self, screen) -> None:
        pygame.draw.circle(screen, self._color, self._position, self._size)
