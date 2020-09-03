# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import math

width = 640
height = 480
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

    def sub(self, v1, v2=None, target=None):
        if v2 == None:
            v2 = PVector(0,0,0)

        if target == None:
            target = PVector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
        else:
            target.set(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
        return target

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

    def setMag(self, len):
        self.normalize()
        self.mult(len)
        return self
        
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
        self.position = PVector(rnd.randint(0,width), rnd.randint(0,height))
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.topSpeed = 5

    def update(self):
        pygame.event.wait()
        mouse = PVector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.acceleration = self.acceleration.sub(mouse,self.position)
        #self.acceleration.setMag(0.2)
        self.acceleration.normalize()
        self.acceleration.mult(0.2)

        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topSpeed)
        self.position.add(self.velocity)

    def display(self):
        window.fill((0,0,0))  # Fills the screen with black
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, 48, 48)) 
        pygame.display.update()   
        pygame.time.delay(10)
 
movers = []

for i in range(0,20):
    movers.append(Mover())

def draw():
    global movers

    for i in range(0,len(movers)):
        movers[i].update()    
        movers[i].display()

while(True):
    draw()

