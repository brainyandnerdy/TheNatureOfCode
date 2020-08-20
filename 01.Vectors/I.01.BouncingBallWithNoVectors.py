# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd

width = 800
height = 200
window = pygame.display.set_mode((width,height))

x = 100.0
y = 100.0
xspeed = 2.5
yspeed = 2.0

def draw():
    global width
    global height
    global window
    global x
    global y
    global xspeed
    global yspeed

    # Add the current speed to the position.
    x = x + xspeed
    y = y + yspeed

    if (x > width) or (x < 0):
        xspeed = xspeed * -1
    
    if (y > height) or (y < 0):
        yspeed = yspeed * -1
    
    window.fill((0,0,0))  # Fills the screen with black
    pygame.draw.ellipse(window, pygame.Color('white'), (x, y, 48, 48)) 
    pygame.display.update()    
    pygame.time.delay(10)
    
while(True):
  draw()
