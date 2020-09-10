# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math
import PVector as pv

width = 640
height = 360

mouseX = 0
mouseY = 0

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


def constrain(elementToConstrain, low, high):
    if elementToConstrain < low:
        elementToConstrain = low
    if elementToConstrain > high:
        elementToConstrain = high
    return elementToConstrain


def dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1))


class Mover:
    def __init__(self):
        self.position = pv.PVector(width/2, height/2)
        self.velocity = pv.PVector(0, 0)
        self.acceleration = 0
        self.topspeed = 4
        self.xoff = 1000
        self.yoff = 0
        self.r = 16

    def update(self):
        global mouseX
        global mouseY

        #mouse = pv.PVector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        mouseX += 2
        mouseY += 1
        mouse = pv.PVector(mouseX, mouseY)
        dir = pv.PVector(0, 0, 0).sub(mouse, self.position)
        dir.normalize()
        dir.mult(0.5)
        self.acceleration = dir

        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)

    def display(self):    
        theta = self.velocity.heading()

        rectCenterX = self.position.x
        rectCenterY = self.position.y
        vertDistanceFromCenter = 10 / 2
        horizDistanceFromCenter = 30 / 2
        pygame.draw.polygon(window, pygame.Color('white'), 
            [rotatePoint(rectCenterX, rectCenterY, theta, rectCenterX - horizDistanceFromCenter, rectCenterY - vertDistanceFromCenter),   # Left up point
             rotatePoint(rectCenterX, rectCenterY, theta, rectCenterX + horizDistanceFromCenter, rectCenterY - vertDistanceFromCenter),   # Right up point
             rotatePoint(rectCenterX, rectCenterY, theta, rectCenterX + horizDistanceFromCenter, rectCenterY + vertDistanceFromCenter),   # Right bottom point
             rotatePoint(rectCenterX, rectCenterY, theta, rectCenterX - horizDistanceFromCenter, rectCenterY + vertDistanceFromCenter)])  # Left bottom point
        pygame.display.update()   
        pygame.time.delay(10)

    def checkEdges(self):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height

window = pygame.display.set_mode((width,height))

movers = Mover()

window.fill((0,0,0))  # Fills the screen with black
pygame.event.get()

def draw():
    global window
    global movers    
    
    window.fill((0,0,0))  # Fills the screen with black
        
    movers.update()
    movers.checkEdges()
    movers.display()

    pygame.display.update()  

while(True):
    draw()

