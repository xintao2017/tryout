import sys
import pygame
from settings import Settings

setting = Settings()

def check_events(ship):
     """ Check user input events"""
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT and ship.rect.centerx < setting.screen_width-4:
                 # Move the ship to the screen_height
                 ship.rect.centerx += 4
             elif event.key ==pygame.K_LEFT and ship.rect.centerx > 4:
                 ship.rect.centerx -= 4
             if event.key == pygame.K_UP and ship.rect.centery > 4:
                 # Move the ship to the screen_height
                 ship.rect.centery -= 4
             elif event.key ==pygame.K_DOWN and ship.rect.centery < setting.screen_height-4:
                 ship.rect.centery += 4


def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
