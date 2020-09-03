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

def draw():
    global width
    global height
    global window

    pygame.event.wait()
    mouse = PVector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    center = PVector(width/2, height/2)
    
    window.fill((0,0,0))  # Fills the screen with black
    pygame.draw.line(window, pygame.Color('white'), (int(center.x), int(center.y)), (int(mouse.x), int(mouse.y)), 1) 
    pygame.display.update()    
    
while(True):
    draw()
