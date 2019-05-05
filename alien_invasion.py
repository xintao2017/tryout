"""
   This module is the main function for a pygame.

"""

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.game_name)

    # Draw a Ship
    ship = Ship(screen)

    while True:
        gf.check_events(ship)

        # Redraw the screen and fill the background color
        gf.update_screen(game_settings, screen, ship)

if __name__ == "__main__":
    run_game()
