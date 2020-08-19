# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd

width = 640
height = 240
t = pygame.display.set_mode((width,height))

#An array to keep track of how often random numbers are picked
randomCounts = []

def setup():  
    global width
    global height
    global randomCounts
    global t

    for i in range(0,80):
        randomCounts.append(0)

def draw():
    global width
    global height
    global t

    index = rnd.randint(0, len(randomCounts))
    randomCounts.append(index)
    
    w = int(width/len(randomCounts))

    for x in range(0,len(randomCounts)):
        pygame.draw.rect(t,pygame.Color('white'), pygame.Rect(x*w,height-randomCounts[x],w-1,randomCounts[x]))
        pygame.display.update()

setup()
while(True):
  draw()
