# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd

width = 200
height = 200
window = pygame.display.set_mode((width,height))

class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

position = PVector(100, 100)
velocity = PVector(2.5, 5)

def draw():
    global width
    global height
    global window
    global position
    global velocity

    # Add the current speed to the position.
    position.add(velocity)

    if (position.x > width) or (position.x < 0):
        velocity.x = velocity.x * -1
    
    if (position.y > height) or (position.y < 0):
        velocity.y = velocity.y * -1
    
    window.fill((0,0,0))  # Fills the screen with black
    pygame.draw.ellipse(window, pygame.Color('white'), (position.x, position.y, 16, 16)) 
    pygame.display.update()    
    pygame.time.delay(10)
    
while(True):
  draw()
