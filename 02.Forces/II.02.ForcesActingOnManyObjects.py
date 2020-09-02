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
    def __init__(self, m, x, y):
        self.position = pv.PVector(x, y)
        self.velocity = pv.PVector(0, 0)
        self.acceleration = pv.PVector(0, 0)
        self.mass = m

    def applyForce(self, force):
        f = pv.PVector(0,0,0).div(self.mass, force)
        self.acceleration.add(f)

    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def display(self):
        
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, self.mass * 16, self.mass * 16)) 
        pygame.display.update()   
        #pygame.time.delay(10)
    
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

movers = []

for i in range(0,20):
    movers.append(Mover(rnd.uniform(0.1,4), 0, 0))

def draw():
    global movers
    global window

    window.fill((0,0,0))  # Fills the screen with black
    for i in range(0,len(movers)):
        wind = pv.PVector(0.01, 0)
        gravity = pv.PVector(0, 0.1)

        movers[i].applyForce(wind)
        movers[i].applyForce(gravity)

        movers[i].update()
        movers[i].display()
        movers[i].checkEdges()
    
while(True):
    draw()

