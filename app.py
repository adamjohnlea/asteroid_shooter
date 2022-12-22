import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")

# importing images. images are also Surfaces

# Game Loop
while True:
    # 1 - Input -> events (mouse click, button press, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2 - Updates
    display_surface.fill('black')
    # blit always places top/left of a surface. The top/left corner of the display_surface is (0,0)

    # 3 - Update display surface
    pygame.display.update()
