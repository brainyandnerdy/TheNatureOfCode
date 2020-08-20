#!/usr/bin/python
import pygame
from pygame.locals import *

def main():
   pygame.init()
   pygame.display.set_mode((300,200))
   pygame.display.set_caption('Testing')
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == QUIT:
            running = False
         if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
         if event.type == MOUSEBUTTONDOWN:
            #print event.button
           print(pygame.mouse.get_pos())
   pygame.display.quit()

if __name__ == '__main__':
   main()