import pygame
import sys
from random import randint, uniform


def display_score():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, 'white')
    text_rect = text_surf.get_rect(midright=(WINDOW_WIDTH, font.get_height()))
    display_surface.blit(text_surf, text_rect)


def laser_timer(can_shoot, duration=500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot


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

# Score font
font = pygame.font.Font('./graphics/subatomic.ttf', 30)

# Ship
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 70))

# Laser
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_list = []

# Laser timer
can_shoot = True
shoot_time = None

# Asteroid
asteroid_surf = pygame.image.load('./graphics/meteor.png').convert_alpha()
asteroid_list = []

# Asteroid timer
asteroid_timer = pygame.event.custom_type()
pygame.time.set_timer(asteroid_timer, 500)

# Sound
laser_sound = pygame.mixer.Sound('./sounds/laser.ogg')
explosion_sound = pygame.mixer.Sound('./sounds/explosion.wav')
background_sound = pygame.mixer.Sound('./sounds/music.wav')
background_sound.play(loops=-1)
background_sound.set_volume(0.2)

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

        if event.type == pygame.KEYDOWN and can_shoot:  # 0.5 secinds of delay before we can shoot again
            if event.key == pygame.K_SPACE:
                laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
                laser_list.append(laser_rect)

                # Timer
                can_shoot = False
                shoot_time = pygame.time.get_ticks()

                # Laser sound
                laser_sound.play()

        if event.type == asteroid_timer:
            x_pos = randint(-100, WINDOW_WIDTH+100)
            y_pos = randint(-100, -50)
            asteroid_rect = asteroid_surf.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            asteroid_list.append((asteroid_rect, direction))

    # Framerate limit
    dt = clock.tick(120) / 1000

    # Mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # Laser timer
    can_shoot = laser_timer(can_shoot, 500)

    # Updates
    display_surface.fill('black')
    display_surface.blit(background_surf, (0, 0))
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(title_surf, title_rect)

    # Asteroid/Ship collisons
    for asteroid_tuple in asteroid_list:
        asteroid_rect = asteroid_tuple[0]
        if ship_rect.colliderect(asteroid_rect):
            pygame.quit()
            sys.exit()

    # Laser/Asteroid collions -> two for loops. 1 for asteroids, 1 for laser
    for asteroid_tuple in asteroid_list:
        for laser in laser_list:
            if laser.colliderect(asteroid_tuple[0]):
                # Explosion sound
                explosion_sound.play()
                laser_list.remove(laser)
                asteroid_list.remove(asteroid_tuple)

    # Score
    display_score()

    # for loop that draws laser surface where the rects are
    laser_speed = 300
    for rect in laser_list:
        display_surface.blit(laser_surf, rect)
        rect.y -= round(laser_speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)

    asteroid_speed = 400
    for asteroid_tuple in asteroid_list:
        direction = asteroid_tuple[1]
        asteroid_rect = asteroid_tuple[0]
        display_surface.blit(asteroid_surf, asteroid_rect)
        asteroid_rect.center += direction * asteroid_speed * dt
        if asteroid_rect.top > WINDOW_HEIGHT:
            asteroid_list.remove(asteroid_tuple)

    # Draw final frame
    pygame.display.update()
