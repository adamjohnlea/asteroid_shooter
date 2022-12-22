import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")
# Create Clock that can be used to limit the framerate
clock = pygame.time.Clock()

# Importing images. Images are also Surfaces
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
background_surf = pygame.image.load('./graphics/background.png').convert()

# Import text. Text is also a Surface
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render('Score: ', True, 'white')

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
    # blit always places top/left of a surface. The top/left corner of the display_surface is (0,0)
    display_surface.blit(background_surf, (0, 0))
    display_surface.blit(ship_surf, (300, 500))
    display_surface.blit(text_surf, (WINDOW_WIDTH - (text_surf.get_width()+120), 20))

    # 3 - Update display surface
    pygame.display.update()
