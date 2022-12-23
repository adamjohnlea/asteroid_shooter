import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("-= ASTEROID SHOOTER =-")
clock = pygame.time.Clock()

# Background
background_surf = pygame.image.load('./graphics/background.png').convert()

# Title
font = pygame.font.Font('./graphics/subatomic.ttf', 30)
title_surf = font.render('-= ASTEROID SHOOTER =-', True, 'white')
title_rect = title_surf.get_rect(midleft=(0, font.get_height()))

# Score
font = pygame.font.Font('./graphics/subatomic.ttf', 30)
text_surf = font.render('SCORE: ', True, 'white')
text_rect = text_surf.get_rect(midright=(WINDOW_WIDTH, font.get_height()))

# Ship
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 70))

# Laser
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_list = []
# laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)

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

        if event.type == pygame.KEYDOWN:  # 0.5 secs of delay betwen shots
            if event.key == pygame.K_SPACE:
                laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
                laser_list.append(laser_rect)
                print(laser_list)

    # Framerate limit
    dt = clock.tick(120) / 1000

    # Mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # Updates
    display_surface.fill('black')
    display_surface.blit(background_surf, (0, 0))
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)
    display_surface.blit(title_surf, title_rect)

    # for loop that draws laser surface where the rects are
    laser_speed = 300
    for rect in laser_list:
        display_surface.blit(laser_surf, rect)
        rect.y -= round(laser_speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)

    # Draw final frame
    pygame.display.update()
