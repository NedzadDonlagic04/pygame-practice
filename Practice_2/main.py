# In this practice I added a background
# onto the previous practice

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# Making variables to store the surface made out of the given image
# and the position where it will be placed on the x,y system
sky_img = pygame.image.load('./../images/Sky.png')
sky_pos = (0, 0)

ground_img = pygame.image.load('./../images/ground.png')
ground_pos = (0, 300)

# Making a font out of a passed font style and size
# Then render it on a scene and saving it along with the position
# where it will be placed on the x,y system
text_font = pygame.font.Font('./../fonts/Pixeltype.ttf', 50)
text_img = text_font.render('My game', False, 'Black')
text_pos = (350, 50) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Using our main screen and placing images on their corresponding positions
    screen.blit(sky_img, sky_pos)
    screen.blit(ground_img, ground_pos)
    screen.blit(text_img, text_pos)

    pygame.display.update()
    clock.tick(60)