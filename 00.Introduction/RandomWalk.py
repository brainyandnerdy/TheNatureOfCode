# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from turtle import *
import random as rnd

width = 800
height = 600

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

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

    def walk(self):
        global width
        global height
        vx = rnd.randint(-2, 2)
        vy = rnd.randint(-2, 2)
        self.x += vx
        self.y += vy
        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)

w = Walker()

def setup():  
    screensize(width, height)
    speed(1)

def draw():
    w.walk()
    w.render()

setup()
while(True):
  draw()