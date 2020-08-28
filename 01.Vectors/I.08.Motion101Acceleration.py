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
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def mult(self, n):
        self.x *= n
        self.y *= n
    
    def div(self, n):
        self.x /= n
        self.y /= n
        
    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def magSq(self):
        return (self.x * self.x + self.y * self.y)

    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def limit(self, max):
        if self.magSq() > max * max:
            self.normalize()
            self.mult(max)


class Mover:
    def __init__(self):
        self.position = PVector(rnd.randint(0,width), rnd.randint(0,height))
        self.velocity = PVector(rnd.randint(-2,2), rnd.randint(-2,2))
        self.acceleration = PVector(-0.001, 0.01)
        self.topSpeed = 10

    def update(self):
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

