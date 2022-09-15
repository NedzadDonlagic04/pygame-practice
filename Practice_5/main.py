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
text_pos = (350, 50) 

snail_img = pygame.image.load('./../images/snail/snail1.png').convert_alpha()
snail_rect = snail_img.get_rect( bottomleft = (800, 300))

player_img = pygame.image.load('./../images/player/player_walk_1.png').convert_alpha()
player_rect = player_img.get_rect( midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_img, sky_pos)
    screen.blit(ground_img, ground_pos)
    screen.blit(text_img, text_pos)

    snail_rect.x -= 3

    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(player_img, player_rect)
    screen.blit(snail_img, snail_rect)

    pygame.display.update()
    clock.tick(60)