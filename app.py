import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")

test_surf = pygame.Surface((400, 100))

# Game Loop
while True:  # run forever -> keeps our game going
    # 1 - Input -> events (mouse click, button press, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2 - Updates
    # blit always places top/left of a surface (test_surf), below its placed in top/left (0,0) of the display_surface
    display_surface.blit(test_surf, (WINDOW_WIDTH - test_surf.get_width(), 0))
    test_surf.fill('red')

    # 3 - Update display surface
    pygame.display.update()
