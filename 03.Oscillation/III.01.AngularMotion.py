# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math

width = 750
height = 150

angle = 0

#pygame.init()
window = pygame.display.set_mode((width,height))

image_orig = pygame.Surface((150, 150))
rotating_image = image_orig.copy()
rect = rotating_image.get_rect()  
rect.center = (width / 2 , height / 2)  

def draw():
    global window
    global angle 
    global rotating_image
    global rect

    window.fill((0,0,0))  # Fills the screen with black

    oldCenter = rect.center
    angle += 0.05
    pygame.draw.line(rotating_image, pygame.Color('white'), (width/2 - 50, height/2), (width/2 + 50, height/2), 2) 
    pygame.draw.ellipse(rotating_image, pygame.Color('white'), (width/2 - 50, height/2, 16, 16)) 
    pygame.draw.ellipse(rotating_image, pygame.Color('white'), (width/2 + 50, height/2, 16, 16)) 
    rotating_image = pygame.transform.rotate(rotating_image, angle)
    rect = rotating_image.get_rect()
    rect.center = oldCenter
    window.blit(rotating_image, rect)
    pygame.display.flip()
    
    pygame.display.update()  

while(True):
    draw()

