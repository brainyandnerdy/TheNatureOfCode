# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math
import PVector as pv

width = 640
height = 360
window = pygame.display.set_mode((width,height))

class Mover:
    def __init__(self):
        self.position = pv.PVector(30, 30)
        self.velocity = pv.PVector(0, 0)
        self.acceleration = pv.PVector(0, 0)
        self.mass = 1

    def applyForce(self, force):
        f = pv.PVector(0,0,0).div(self.mass, force)
        self.acceleration.add(f)

    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def display(self):
        window.fill((0,0,0))  # Fills the screen with black
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, 48, 48)) 
        pygame.display.update()   
        pygame.time.delay(10)
    
    def checkEdges(self):
        if self.position.x > width:
            self.position.x = width
            self.velocity.x *= -1
        elif self.position.x < 0:
            self.velocity.x *= -1
            self.position.x = 0
        
        if self.position.y > height:
            self.velocity.y *= -1
            self.position.y = height

m = Mover()

def draw():
    global m

    wind = pv.PVector(0.01, 0)
    gravity = pv.PVector(0, 0.1)
    m.applyForce(wind)
    m.applyForce(gravity)

    m.update()
    m.display()
    m.checkEdges()

while(True):
    draw()

