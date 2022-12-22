import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")

# Create a surface
test_surf = pygame.Surface((400, 100))
# We need to attach the test_surf to the display_surface (done in game loop Updates)
# We need to make the test_surf a color other than black

# Game Loop
while True:  # run forever -> keeps our game going
    # 1 - Input -> events (mouse click, button press, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2 - Updates
    # display_surface.fill('blue')
    display_surface.blit(test_surf, (0, 0))
    test_surf.fill('red')

    # 3 - Update display surface
    pygame.display.update()
