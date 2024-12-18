
import sys
import pygame

from Settings import Settings
from Ship import Ship

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
        #self.setting = (230,230,230)
        self.ship = Ship(self)

    # def run_game(self):
    #     """ Start the main loop for the game """
    #     while True:
    #     # watch for keyboard an mouse events.
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()

    #         # Redraw the screen during each pass through the loop 
    #         self.screen.fill(self.settings.bg_color)
    #         self.ship.blitme()

    #         # Make the most recently drawn screen visible
    #         pygame.display.flip()
    #         self.clock.tick(60)

    def run_game(self):
        """ Start the main loop for the game """
        while True:
        # watch for keyboard an mouse events.
            self._check_events()

            # Redraw the screen during each pass through the loop 
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()

            # # Make the most recently drawn screen visible
            # pygame.display.flip()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """ Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
           # Redraw the screen during each pass through the loop 
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
