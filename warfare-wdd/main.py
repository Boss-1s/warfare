# Example file showing a basic pygame "game loop"
from pathlib import Path

import pygame

from .utils import svg_to_png

# pygame setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
# game_map: pygame.Surface = pygame.image.load(svg_to_png(Path("./warfare-wdd/assets/MapChart_Map.svg"), return_file=True)).convert()
# map_rect = game_map.get_rect()
# map_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0,0,0))

    # RENDER YOUR GAME HERE
    # screen.blit(game_map, map_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
