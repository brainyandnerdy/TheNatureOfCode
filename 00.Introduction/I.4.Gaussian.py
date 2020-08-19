# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd

width = 640
height = 360
window = pygame.display.set_mode((width,height))


def setup():  
    global width
    global height

def draw():
    global width
    global height
    global window

    # Get a gaussian random number w/ mean of 0 and standard deviation of 1.0
    xloc = rnd.gauss(0, 1.0)
    
    sd = 60.0                       # Define a standard deviation
    mean = width/2                  # Define a mean value (middle of the screen along the x-axis)
    xloc = (xloc * sd) + mean       # Scale the gaussian random number by standard deviation and mean

    pygame.draw.ellipse(window, pygame.Color('white'), (xloc, height/2, 16, 16))  # Draw an ellipse at our "normal" random position
    pygame.display.update()
    
setup()
while(True):
  draw()
