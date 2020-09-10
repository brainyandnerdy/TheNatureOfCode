# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Wolfram Cellular Automata

import pygame
import random as rnd
import os.path

width = 1800
height = 600
window = pygame.display.set_mode((width,height))
window.fill((0,0,0))  # Fills the screen with black

scl = 20

# A class to manage the Cellular Automata
class CA:
    def __init__(self, r=None):
        global width
        global height
        global scl         

        self.scl = scl

        if r == None:
            self.scl = 1 
            self.ruleset = []

            for i in range(0, 8):
                self.ruleset.append(rnd.randint(0,2))

        else:
            self.ruleset = r # An array to store the ruleset, for example {0,1,1,0,1,1,0,1}
        
        self.cells = [] # An array of 0s and 1s 
        
        cellNumber = int(width/self.scl)
        for i in range(0, cellNumber):
            self.cells.append(0)
        
        self.generation = 0 # How many generations?

    
    def setRules(self, r):
        """ Set the rules of the CA """
        self.ruleset = r


    def randomize(self):
        """ Make a random ruleset """
        for i in range(0, 8):
            self.ruleset[i] = rnd.randint(0,2)


    def restart(self):
        """ Reset to generation 0 """
        cellNumber = len(self.cells)
        for i in range(0, cellNumber):
            self.cells[i] = 0

        self.cells[int(cellNumber/2)] = 1 # We arbitrarily start with just the middle cell having a state of "1"
        self.generation = 0


    def rules(self, a, b, c):
        """ Implementing the Wolfram rules
        Could be improved and made more concise, but here we can explicitly see what is going on for each case
        """
        return self.ruleset[a+b+c]


    def generate(self):
        """ The process of creating the new generation """        
        nextgen = [] # First we create an empty array for the new values
        for i in range(0, len(self.cells)):
            nextgen.append(0)
        # For every spot, determine new state by examing current state, and neighbor states
        # Ignore edges that only have one neighor
        for i in range(1, len(self.cells) - 1):
            left = self.cells[i-1] # Left neighbor state
            me = self.cells[i] # Current state
            right = self.cells[i+1]  # Right neighbor state
            nextgen[i] = self.rules(left, me, right) # Compute next generation state based on ruleset
        
        # The current generation is the new generation
        self.cells = nextgen
        self.generation += 1


    def render(self):
        """ This is the easy part, just draw the cells, fill 255 for '1', fill 0 for '0' """
        for i in range(0, len(self.cells)):
            if self.cells[i] == 1:
                pygame.draw.rect(window, pygame.Color('black'), (i*self.scl, self.generation*self.scl, self.scl, self.scl)) 
            else:
                pygame.draw.rect(window, pygame.Color('white'), (i*self.scl, self.generation*self.scl, self.scl, self.scl)) 
        pygame.display.update()   


    def finished(self):
        """ The CA is done if it reaches the bottom of the screen """
        if(self.generation > height/self.scl):
            return True
        else:
            return False

        
# Simple demonstration of a Wolfram 1-dimensional cellular automata
# When the system reaches bottom of the window, it restarts with a new ruleset
# Mouse click restarts as well

#ruleset = [0, 1, 0, 1, 1, 0, 1, 0] # 90
ruleset = [0, 1, 1, 1, 1, 0, 1, 1] # An initial rule system

ca = CA(ruleset) # An instance object to describe the Wolfram basic Cellular Automata

fileName = "rule222.jpeg"
def draw():
    global window
    global ca   
    global fileName

    ca.render() # Draw the CA
    ca.generate() # Generate the next level

    if ca.finished(): # If we're done, clear the screen, pick a new ruleset and restart
        if not os.path.isfile(fileName):
            pygame.image.save(window, fileName)
            #saveFrame("rule222.png");
            #noLoop();

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.fill((0,0,0))  # Fills the screen with black
            ca.randomize()
            ca.restart()

while (True):
    draw()