# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd

width = 640
height = 360
window = pygame.display.set_mode((width,height))

class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def mult(self, n):
        self.x *= n
        self.y *= n
    
    def div(self, n):
        self.x /= n
        self.y /= n
        

def draw():
    global width
    global height
    global window

    #if pygame.mouse.get_pressed()[0]:
    mouse = PVector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    center = PVector(width/2, height/2)
    
    # Multiplying a vector!  The vector is now half its original size (multiplied by 0.5).
    mouse.mult(0.5)    
    
    window.fill((0,0,0))  # Fills the screen with black
    pygame.draw.line(window, pygame.Color('white'), (center.x, center.y), (mouse.x, mouse.y), 1) 
    pygame.display.update()    
    
while(True):
    draw()
