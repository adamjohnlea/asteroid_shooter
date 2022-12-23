import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")
clock = pygame.time.Clock()

# Background
background_surf = pygame.image.load('./graphics/background.png').convert()

# Score
font = pygame.font.Font('./graphics/subatomic.ttf', 50)
text_surf = font.render('Score: ', True, 'white')
text_rect = text_surf.get_rect(midright=(WINDOW_WIDTH, font.get_height()))

# Ship
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 70))

# Laser
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)

# Game Loop
while True:
    # Input -> events (mouse click, button press, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("shoot")

    # Framerate limit
    clock.tick(60)

    # Mouse input
    # ship_rect.center = pygame.mouse.get_pos()
    laser_rect.y -= 4

    # Updates
    display_surface.fill('black')
    display_surface.blit(background_surf, (0, 0))
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)

    # 3 - Update display surface
    pygame.display.update()
