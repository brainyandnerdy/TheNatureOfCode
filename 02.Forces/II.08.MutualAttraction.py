# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math
import PVector as pv

width = 640
height = 360

g = 0.4

#pygame.init()
window = pygame.display.set_mode((width,height))

def constrain(elementToConstrain, low, high):
    if elementToConstrain < low:
        elementToConstrain = low
    if elementToConstrain > high:
        elementToConstrain = high
    return elementToConstrain


def dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1))


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
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, self.mass * 24, self.mass * 24)) 
        pygame.display.update()   
        #pygame.time.delay(10)
    
    def attract(self, m):
        force = pv.PVector(0,0,0).sub(self.position, m.position) # Calculate direction of force
        distance = force.mag() # Distance between objects
        distance = constrain(distance, 5.0, 25.0) # Limiting the distance to eliminate "extreme" results for very close or very far objects
        force.normalize() # Normalize vector (distance doesn't matter here, we just want this vector for direction

        strength = (g * self.mass * m.mass) / (distance * distance) # Calculate gravitional force magnitude
        force.mult(strength) # Get force vector --> magnitude * direction
        return force

# Setup
movers = []

for i in range(0,20):
    movers.append(Mover(rnd.uniform(0.1,2), rnd.randint(0, width), rnd.randint(0, height)))

def draw():
    global movers
    global window

    window.fill((0,0,0))  # Fills the screen with black

    for i in range(0, len(movers)):   
        for j in range (0, len(movers)):    
            if i != j:
                force = movers[j].attract(movers[i])
                movers[i].applyForce(force)
        movers[i].update()
        movers[i].display()

while(True):
    draw()

