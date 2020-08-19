# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import turtle
import random as rnd

width = 640
height = 240
t = turtle.Turtle()

#An array to keep track of how often random numbers are picked
randomCounts = []

def setup():  
    global width
    global height
    global randomCounts
    global t

    turtle.screensize(width, height)
    #speed(1)

    for i in range(0,20):
        randomCounts.append(rnd.randint(0, height))

def draw():
    global width
    global height
    global t

    index = rnd.randint(0, len(randomCounts))
    randomCounts.append(index)

    t.pencolor('black')
    t.penup()
    t.setx(width/2)
    t.sety(height/2)
    t.dot()
    t.pendown()

    w = width/len(randomCounts)

    for x in range(0,len(randomCounts)):
        t.forward(x * w) #Forward turtle by 150 units
        t.left(height-randomCounts[x]) #Turn turtle by 90 degree
        t.forward(w-1) #Forward turtle by 80 units
        t.left(randomCounts[x]) #Turn turtle by 90 degree
    
    #w.step()
    #w.render()

setup()
while(True):
  draw()
