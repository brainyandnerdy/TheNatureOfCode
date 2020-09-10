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
        """
        Newton's 2nd law: F = M * A
        or A = F / M
        """
        f = pv.PVector(0,0,0).div(self.mass, force) # divide by mass
        self.acceleration.add(f)                    # Accumulate all forces in acceleration

    def update(self):
        self.velocity.add(self.acceleration) # Velocity changes according to acceleration
        self.position.add(self.velocity)     # position changes by velocity
        self.acceleration.mult(0)            # We must clear acceleration each frame

    def display(self):
        
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, self.mass * 16, self.mass * 16)) 
        pygame.display.update()   
        #pygame.time.delay(10)
    
    def checkEdges(self):
        """
        Bounce off bottom of window
        """        
        if self.position.y > height:
            self.velocity.y *= -0.9 # A little dampening when hitting the bottom
            self.position.y = height

# Liquid class
class Liquid:
    def __init__(self, x__, y__, w__, h__, c__):
        # Liquid is a rectangle
        self.x = x__
        self.y = y__
        self.w = w__
        self.h = h__
        # Coefficient of drag
        self.c = c__ 

    def contains(self, m):
        """
        Is the Mover in the Liquid?
        """
        l = m.position
        return l.x > self.x and l.x < self.x + self.w and l.y > self.y and l.y < self.y + self.h

    def drag(self, m):
        """
        Calculate drag force
        """
        # Magnitude is coefficient * speed squared
        speed = m.velocity.mag()
        dragMagnitude = self.c * speed * speed

        # Direction is inverse of velocity
        dragForce = m.velocity.get()
        dragForce.mult(-1)

        # Scale according to magnitude
        dragForce.normalize()
        dragForce.mult(dragMagnitude)
        return dragForce
    
    def display(self):
        #window.fill((0,0,0))  # Fills the screen with black
        pygame.draw.rect(window, pygame.Color('gray'), (self.x, self.y, self.w, self.h)) 
        pygame.display.update()   
        pygame.time.delay(10)


movers = []

liquid = Liquid(0,height/2, width, height/2, 0.1)

for i in range(0,9):
    movers.append(Mover(rnd.uniform(0.5,3), 40 + i * 70, 0))

def reset():
    global movers 

    for i in range(0,9):
        movers[i] = Mover(rnd.uniform(0.5,3), 40 + i * 70, 0)

def draw():
    global movers
    global window
    global liquid

    window.fill((0,0,0))  # Fills the screen with black

    liquid.display()

    for i in range(0,len(movers)):
        if liquid.contains(movers[i]):
            # Calculate drag force
            dragForce = liquid.drag(movers[i])
            # Apply drag force to Mover
            movers[i].applyForce(dragForce)

        # Gravity is scaled by mass here!
        gravity = pv.PVector(0, 0.1 * movers[i].mass)
        # Apply gravity
        movers[i].applyForce(gravity)

        movers[i].update()
        movers[i].display()
        movers[i].checkEdges()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.fill((0,0,0))  # Fills the screen with black
            reset()
    
while(True):   
    draw()

