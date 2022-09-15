# Creating a blank window with the title "Runner"
# It will allow the user to exit upon pressing the x icon in the top right corner
# It won't run more than 60 fps

# Importing all the needed modules
import pygame
from sys import exit

# Initializes all the pygame modules used in the project
pygame.init()

# Creates a screen (in the comments referred to as window) and stores it inside a variable for later
screen = pygame.display.set_mode((800, 400))

# Gives the window a name
pygame.display.set_caption('Runner')

# Creates a Clock object used later for controlling the frame rate
clock = pygame.time.Clock()

# Event loop
while True:
    
    # Gets all the events and goes through them individually
    for event in pygame.event.get():

        # Checks if the event is clicking the x icon
        if event.type == pygame.QUIT:

            # Uninitializes all the pygame modules used in the project
            # Which means the window will close
            pygame.quit()

            # Stops the code from continuing to run
            exit()

    # Updated the window
    pygame.display.update()

    # Sets the ceiling for the fps
    clock.tick(60)