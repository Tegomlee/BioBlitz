# Imports
import pygame

class Engine:

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode((1280, 720))
        self._clock = pygame.time.Clock()
        self._running = True


    def run(self) -> None:
        while self._running:
            self._process_events()
            self._process_updates()
            self._process_render_calls()
            self._clock.tick(60)

        self._clean_up()


    def _process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False


    def _process_updates(self) -> None:
        pass


    def _process_render_calls(self) -> None:
        self._screen.fill("purple")

        pygame.display.flip()


    def _clean_up(self) -> None:
        pygame.quit()


# Unit Tests
if __name__ == '__main__':
    engine = Engine()
    engine.run()
