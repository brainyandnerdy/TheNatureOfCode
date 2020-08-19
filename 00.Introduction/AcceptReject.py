# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd

width = 800
height = 200
t = pygame.display.set_mode((width,height))

#An array to keep track of how often random numbers are picked
randomCounts = []

def setup():  
    global width
    global height
    global randomCounts
    global t

    for i in range(0,20):
        randomCounts.append(0.0)

def accept_reject():
    """
    An algorithm for picking a random number based on monte carlo method
    Here probability is determined by formula y = x
    """
    # Have we found one yet
    foundone = False
    hack = 0        # let's count just so we don't get stuck in an infinite loop by accident
    while (not foundone and hack < 10000):        
        # Pick two random numbers
        r1 = rnd.random()
        r2 = rnd.random()
        y = r1*r1   # y = x*x (change for different results)
        # If r2 is valid, we'll use this one
        if (r2 < y):
            foundone = True
            return r1        
        hack += 1

    # Hack in case we run into a problem (need to improve this)
    return 0

def draw():
    global width
    global height
    global t

    # Pick a random number and increase the count
    index = int(accept_reject() * len(randomCounts))
    randomCounts.append(index)
    
    # Draw a rectangle to graph results
    w = width / len(randomCounts)

    for x in range(0,len(randomCounts)):
        pygame.draw.rect(t,pygame.Color('white'), pygame.Rect(x*w,height-randomCounts[x],w-1,randomCounts[x]))
        pygame.display.update()

setup()
while(True):
  draw()
