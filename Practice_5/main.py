# Made it so once the snail and player collide the game ends
# Amongst other things, after this practice I will be making 
# the final version of the game with additions from myself
# to what the followed tutorial showed

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_img = pygame.image.load('./../images/Sky.png').convert()
sky_pos = (0, 0)

ground_img = pygame.image.load('./../images/ground.png').convert()
ground_pos = (0, 300)

text_font = pygame.font.Font('./../fonts/Pixeltype.ttf', 50)
text_img = text_font.render('My game', False, 'Black')
text_rect = text_img.get_rect( center = (400, 50))

snail_img = pygame.image.load('./../images/snail/snail1.png').convert_alpha()
snail_rect = snail_img.get_rect( bottomleft = (800, 300))

player_img = pygame.image.load('./../images/player/player_walk_1.png').convert_alpha()
player_rect = player_img.get_rect( midbottom = (80, 300))

gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                gravity = -22
        
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
            if player_rect.collidepoint(event.pos):
                gravity = -22

    screen.blit(sky_img, sky_pos)
    screen.blit(ground_img, ground_pos)
    screen.blit(text_img, text_rect)

    # Snail
    snail_rect.x -= 4

    if snail_rect.right <= 0:
        snail_rect.left = 800
    
    screen.blit(snail_img, snail_rect)

    # Player
    gravity += 1
    player_rect.y += gravity

    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    screen.blit(player_img, player_rect)

    if player_rect.colliderect(snail_rect):
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)