import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")

# Game Loop
while True:  # run forever -> keeps our game going
    # 1 - Input -> events (mouse click, button press, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2 - Updates

    # 3 - Update display surface
    pygame.display.update()
