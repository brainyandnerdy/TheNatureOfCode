# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from turtle import *
import random as rnd

width = 640
height = 360

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

# A random walker object!
class Walker:

    def __init__(self):
        self.x = 0
        self.y = 0
    
    def render(self):
        pencolor('black')
        penup()
        setx(self.x)
        sety(self.y)
        dot()
        pendown()

    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        global width
        global height
        r = rnd.random()
        # A 40% of moving to the right!
        if (r < 0.4):
            self.x = self.x + 1
        elif (r < 0.5):
            self.x = self.x - 1
        elif (r < 0.9):
            self.y = self.y + 1
        else:
            self.y = self.y - 1
        
        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)

w = Walker()

def setup():  
    screensize(width, height)
    #speed(1)

def draw():
    w.step()
    w.render()

setup()
while(True):
  draw()
