# In this practice I added a moving snail
# that will go from the right to the left side
# in an infinite loop, this is an addition
# to the previous practice

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# Convert methods converts the given image to fit pygame more
# It (in theory) helps with the games performance
sky_img = pygame.image.load('./../images/Sky.png').convert()
sky_pos = (0, 0)

ground_img = pygame.image.load('./../images/ground.png').convert()
ground_pos = (0, 300)

text_font = pygame.font.Font('./../fonts/Pixeltype.ttf', 50)
text_img = text_font.render('My game', False, 'Black')
text_pos = (350, 50) 

# Loading the snail image into a variable as well as storing the position I want it
# displayed on screen
# Because the snail image has alpha value we have to use convert_alpha to cut them
# from the image
snail_img = pygame.image.load('./../images/snail/snail1.png').convert_alpha()
snail_y = 270
snail_x = 730

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_img, sky_pos)
    screen.blit(ground_img, ground_pos)
    screen.blit(text_img, text_pos)

    # Every time the event loop goes through an iteration it redraws the screen
    # In normal conditions it should redraw it 60 times in a second
    # Because of this what we do is we decrease the snail img x position by 3
    # on each iteration which combined with the redrawing of the screen will
    # create the illusion of the snail moving on the screen
    snail_x -= 3
    screen.blit(snail_img, (snail_x, snail_y))

    # Checking if the snail has gone off screen, if it has spawn it at the start
    if snail_x < -60:
        snail_x = 800

    pygame.display.update()
    clock.tick(60)