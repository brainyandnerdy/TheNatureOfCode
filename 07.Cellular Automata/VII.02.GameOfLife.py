# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# A basic implementation of John Conway's Game of Life CA

import pygame
import random as rnd
import os.path

width = 640
height = 360
window = pygame.display.set_mode((width,height))
window.fill((0,0,0))  # Fills the screen with black

w = 8

class GOL:
    def __init__(self, r=None):
        global w 
        self.w = w 
        self.columns = int(width/self.w)
        self.rows = int(height/self.w)
        self.board = [[rnd.randint(0,2) for x in range(1, self.rows - 1)] for y in range(1, self.columns - 1)] 

    def generate(self):
        nextGen = [[0 for x in range(1, self.rows - 1)] for y in range(1, self.columns - 1)] 
        for x in range(1, self.columns - 3):
            for y in range(1, self.rows - 3):
                # Add up all the states in a 3x3 surrounding grid
                neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbors += self.board[x + i][y + j] 

                # A little trick to subtract the current cell's state since
                # we added it in the above loop
                neighbors -= self.board[x][y]
            
                # Rules of Life
                if ((self.board[x][y] == 1) and (neighbors < 2)): # Loneliness
                    nextGen[x][y] = 0
                elif ((self.board[x][y] == 1) and (neighbors > 3)): # Overpopulation
                    nextGen[x][y] = 0
                elif ((self.board[x][y] == 0) and (neighbors == 3)): # Reproduction
                    nextGen[x][y] = 1          
                else:                                           # Stasis
                    nextGen[x][y] = self.board[x][y] 

        self.board = nextGen # Next is now our board


    def display(self):
        window.fill((0,0,0))  # Fills the screen with black
        for i in range(0, self.columns - 3):
            for j in range(0, self.rows - 3):
                if(self.board[i][j] == 1):
                    pygame.draw.rect(window, pygame.Color('white'), (i * self.w, j * self.w, self.w, self.w)) 
                    #pygame.draw.rect(window, (255,255,255), (i * self.w, j * self.w, self.w, self.w)) 
                    
        pygame.display.update() 

        
gol = GOL()

def draw():
    global window
    global gol   

    gol.generate()
    gol.display()

    # reset board when mouse is pressed
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.fill((0,0,0))  # Fills the screen with black
            gol = GOL()

while (True):
    draw()