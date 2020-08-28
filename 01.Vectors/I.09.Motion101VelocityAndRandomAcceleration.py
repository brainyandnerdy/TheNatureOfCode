# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math

width = 640
height = 360
window = pygame.display.set_mode((width,height))

class PVector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def set(self, v):
        self.x = v.x
        self.y = v.y
        self.z = v.z
        return self

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y
        self.z -= vector.z

    def mult(self, n):
        self.x *= n
        self.y *= n
        self.z *= n
    
    def div(self, n):
        self.x /= n
        self.y /= n
        self.z /= n
        
    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def magSq(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def limit(self, max):
        if self.magSq() > max * max:
            self.normalize()
            self.mult(max)
    
    def fromAngle(self, angle, target=None):
        if target == None:
            target = PVector(math.cos(angle), math.sin(angle),0)
        else:
            target.set(math.cos(angle), math.sin(angle),0)
        return target
    
    def random2D(self, target=None, parent=None):
        if parent == None:
            return self.fromAngle(rnd.random() * math.pi * 2, target)
        else:
            #return fromAngle(parent.random(PConstants.TAU), target);
            return self.fromAngle(rnd.random() * math.pi * 2, target)

class Mover:
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.topSpeed = 6

    def update(self):
        self.acceleration = self.acceleration.random2D()
        self.acceleration.mult(rnd.randint(0,2))

        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topSpeed)
        self.position.add(self.velocity)

    def display(self):
        window.fill((0,0,0))  # Fills the screen with black
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, 48, 48)) 
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

mover = Mover()

def draw():
    global mover

    mover.update()
    mover.checkEdges()
    mover.display()

while(True):
    draw()

