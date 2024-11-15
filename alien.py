
import sys
import pygame

from Settings import Settings

class AlienInvasion:
    """ overall clas to manage game assets and behaviour """

    def __init__(self):
        """ Intialize the game, and create game reources. """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode(self.settings.screen_width,
        #  self.settings.screen_height)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Set the background color
        self.setting = (230,230,230)

    def run_game(self):
        """ Start the main loop for the game """
        while True:
        # watch for keyboard an mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop 
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
