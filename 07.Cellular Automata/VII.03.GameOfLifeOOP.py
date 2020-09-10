# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# An OOP implementation of John Conway's Game of Life CA

import pygame
import random as rnd
import os.path

width = 640
height = 360
window = pygame.display.set_mode((width,height))
window.fill((0,0,0))  # Fills the screen with black

w = 8

class Cell:
    def __init__(self, x__, y__, w__):
        self.x = x__
        self.y = y__
        self.w = w__

        self.state = rnd.randint(0, 2)
        self.previous = self.state


    def savePrevious(self):
        self.previous = self.state
    

    def newState(self, s):
        self.state = s

    
    def display(self):
        if self.previous == 0 and self.state == 1:
            pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.w, self.w))
        elif self.state == 1:
            pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.w, self.w))
        elif self.previous == 1 and self.state == 0:
            pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.w, self.w))
        else:
            pygame.draw.rect(window, (255,255,255), (self.x, self.y, self.w, self.w))
     

class GOL:
    def __init__(self, r=None):
        global w 
        self.w = w 
        self.columns = int(width/self.w)
        self.rows = int(height/self.w)
        self.board = [[Cell(i * self.w, j * self.w, self.w) for j in range(0, self.rows)] for i in range(0, self.columns)] 


    def generate(self):
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                self.board[i][j].savePrevious()
        
        # Loop through every spot in our 2D array and check spots neighbors
        for x in range(0, self.columns):
            for y in range(0, self.rows):
                # Add up all the states in a 3x3 surrounding grid
                neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        firstIndex = (x + i + self.columns) % self.columns
                        secondIndex = (y + j + self.rows) % self.rows
                        neighbors += self.board[firstIndex][secondIndex].previous

                # A little trick to subtract the current cell's state since
                # we added it in the above loop
                neighbors -= self.board[x][y].previous
            
                # Rules of Life
                if ((self.board[x][y].state == 1) and (neighbors < 2)): # Loneliness
                    self.board[x][y].newState(0)
                elif ((self.board[x][y].state == 1) and (neighbors > 3)): # Overpopulation
                    self.board[x][y].newState(0)
                elif ((self.board[x][y].state == 0) and (neighbors == 3)): # Reproduction
                    self.board[x][y].newState(1)         
                else:                                           # Stasis
                    # else do nothing!
                    pass


    def display(self):        
        for i in range(0, self.columns):
            for j in range(0, self.rows):
                self.board[i][j].display()
        pygame.display.update() 

        
gol = GOL()

def draw():
    global window
    global gol   
    window.fill((0,0,0))  # Fills the screen with black
    gol.generate()
    gol.display()

    # reset board when mouse is pressed
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.fill((0,0,0))  # Fills the screen with black
            gol = GOL()

while (True):
    draw()