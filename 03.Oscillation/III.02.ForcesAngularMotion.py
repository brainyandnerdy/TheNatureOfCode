# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math
import PVector as pv

width = 640
height = 360

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
    def __init__(self, m, x, y):
        self.position = pv.PVector(x, y)
        self.velocity = pv.PVector(rnd.randint(-1,1), rnd.randint(-1,1))
        self.acceleration = pv.PVector(0, 0)
        self.mass = m
        self.angle = 0
        self.aVelocity = 0
        self.aAcceleration = 0

    def applyForce(self, force):
        f = pv.PVector(0,0,0).div(self.mass, force)
        self.acceleration.add(f)

    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)

        self.aAcceleration = self.acceleration.x / 10.0
        self.aVelocity += self.aAcceleration
        self.aVelocity = constrain(self.aVelocity, -0.1, 0.1)
        self.angle += self.aVelocity

        self.acceleration.mult(0)

    def display(self):     
        # pushMatrix()  
        topLeftRectPoint = rotatePoint(width/2, height/2, self.angle, width/2 - 50, height/2) 
        bottomRightRectPoint = rotatePoint(width/2, height/2, self.angle, width/2 - 50, height/2) 
        pygame.draw.rect(window, pygame.Color('white'), (width/2, height/2, self.mass * 16, self.mass * 16)) 
        pygame.display.update()   
        pygame.time.delay(10)
        # popMatrix()   

# A class for a draggable attractive body in our world
class Attractor:
    def __init__(self):
        self.position = pv.PVector(width/2, height/2) # position
        self.mass = 20 # Mass, tied to size
        self.G = 0.4 # Gravitational Constant

    def attract(self, m):
        force = pv.PVector(0,0,0).sub(self.position, m.position) # Calculate direction of force
        d = force.mag() # Distance between objects
        d = constrain(d, 5.0, 25.0) # Limiting the distance to eliminate "extreme" results for very close or very far objects
        force.normalize() # Normalize vector (distance doesn't matter here, we just want this vector for direction)
        strength = (self.G * self.mass * m.mass) / (d * d) # Calculate gravitional force magnitude
        force.mult(strength) # Get force vector --> magnitude * direction
        return force

    def display(self):
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, 48, 48))
        pygame.display.update()  

window = pygame.display.set_mode((width,height))

movers = []
for i in range(0,20):
    movers.append(Mover(rnd.uniform(0.1,2), rnd.randint(0, width), rnd.randint(0, height)))

a = Attractor()

def draw():
    global window
    global movers
    global a

    window.fill((0,0,0))  # Fills the screen with black
    
    a.display()
    
    for i in range(0, len(movers)):
        force = a.attract(movers[i])
        movers[i].applyForce(force)

        movers[i].update()
        movers[i].display()
    pygame.display.update()  

while(True):
    draw()

