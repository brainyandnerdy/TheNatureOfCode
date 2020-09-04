# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math

width = 750
height = 150

angle = 0

def rotatePoint(cx, cy, angle, px, py):
    """
    cx, cy = pivot point
    angle is in radians 
    px, py = point to rotate
    """
    s = math.sin(angle)
    c = math.cos(angle)

    # translate point back to origin
    px -= cx
    py -= cy

    # rotate point
    newx = px * c - py * s
    newy = px * s + py * c

    # translate point back
    px = newx + cx
    py = newy + cy
    return (px, py)

window = pygame.display.set_mode((width,height))

def draw():
    global window
    global angle 

    window.fill((0,0,0))  # Fills the screen with black
    
    pygame.draw.line(window, pygame.Color('white'), rotatePoint(width/2, height/2, angle, width/2 - 50, height/2), rotatePoint(width/2, height/2, angle, width/2 + 50, height/2), 2) 
    leftEllipsePoint = rotatePoint(width/2, height/2, angle, width/2 - 50, height/2)
    pygame.draw.ellipse(window, pygame.Color('white'), (leftEllipsePoint[0] - 8, leftEllipsePoint[1] - 8, 16, 16)) 
    rightEllipsePoint = rotatePoint(width/2, height/2, angle, width/2 + 50, height/2)
    pygame.draw.ellipse(window, pygame.Color('white'), (rightEllipsePoint[0] - 8, rightEllipsePoint[1] - 8, 16, 16)) 
    pygame.display.update()  
    angle += 0.0005

while(True):
    draw()

