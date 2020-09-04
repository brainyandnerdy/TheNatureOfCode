# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math
import PVector as pv

width = 640
height = 360

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
        self.velocity = pv.PVector(1, 0)
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
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, self.mass * 25, self.mass * 25)) 
        pygame.display.update()   
        pygame.time.delay(10)
    
    def checkEdges(self):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.velocity.x = width
        
        if self.position.y > height:
            self.velocity.y *= -1
            self.position.y = height

# A class for a draggable attractive body in our world
class Attractor:
    def __init__(self):
        self.position = pv.PVector(width/2, height/2) # position
        self.mass = 20 # Mass, tied to size
        self.G = 1 # Gravitational Constant
        self.dragOffset = pv.PVector(0.0,0.0) # holds the offset for when object is clicked on
        self.dragging = False # Is the object being dragged?
        self.rollover = False # Is the mouse over the ellipse?

    def attract(self, m):
        force = pv.PVector(0,0,0).sub(self.position, m.position) # Calculate direction of force
        d = force.mag() # Distance between objects
        d = constrain(d, 5.0, 25.0) # Limiting the distance to eliminate "extreme" results for very close or very far objects
        force.normalize() # Normalize vector (distance doesn't matter here, we just want this vector for direction)
        strength = (self.G * self.mass * m.mass) / (d * d) # Calculate gravitional force magnitude
        force.mult(strength) # Get force vector --> magnitude * direction
        return force

    def display(self):
        if self.dragging:
            pygame.draw.ellipse(window, pygame.Color('gray'), (self.position.x, self.position.y, self.mass * 2, self.mass * 2)) 
        elif self.rollover:
            pygame.draw.ellipse(window, pygame.Color('red'), (self.position.x, self.position.y, self.mass * 2, self.mass * 2)) 
        else:
            pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, self.mass * 2, self.mass * 2))
        pygame.display.update()  

    def clicked(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass:
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my

    def hover(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass:
            self.rollover = True
        else:
            self.rollover = False

    def stopDragging(self):
        self.dragging = False
    
    def drag(self):
        if self.dragging:
            self.position.x = pygame.mouse.get_pos()[0] + self.dragOffset.x
            self.position.y = pygame.mouse.get_pos()[1] + self.dragOffset.y

# Setup
movers = []

for i in range(0,10):
    movers.append(Mover(rnd.uniform(0.1,2), rnd.randint(0, width), rnd.randint(0, height)))

attractor = Attractor()


def draw():
    global movers
    global attractor
    global window

    window.fill((0,0,0))  # Fills the screen with black
    pygame.event.get()
    attractor.display()
    attractor.drag()
    attractor.hover(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    for i in range(0, len(movers)):        
        force = attractor.attract(movers[i])
        movers[i].applyForce(force)
        movers[i].update()
        movers[i].display()

    if(pygame.mouse.get_pressed()[0]):
        attractor.clicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    else:
        attractor.stopDragging()
    
while(True):
    draw()

