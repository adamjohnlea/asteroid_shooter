import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")
# Create Clock that can be used to limit the framerate
clock = pygame.time.Clock()

# Importing images. Images are also Surfaces
# Ship
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 70))

background_surf = pygame.image.load('./graphics/background.png').convert()

# Import text. Text is also a Surface
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render('Score: ', True, 'white')
text_rect = text_surf.get_rect(midright=(WINDOW_WIDTH, font.get_height()))

# Game Loop
while True:
    # 1 - Input -> events (mouse click, button press, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Use created clock to limit framerate to 60 FPS
    clock.tick(60)

    # 2 - Updates
    display_surface.fill('black')
    display_surface.blit(background_surf, (0, 0))

    if ship_rect.top > 8:
        ship_rect.y -= 4
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)

    # 3 - Update display surface
    pygame.display.update()
