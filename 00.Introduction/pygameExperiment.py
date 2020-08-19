import pygame
width = 640
height = 600

game = pygame.display.set_mode((width,height))
pygame.display.set_caption("My First Game")
game.fill((0,0,0))
#pygame.draw.rect(game,pygame.Color('white'), pygame.Rect((10,50),(50,200)))
pygame.draw.rect(game,(255,255,255),(10,50, 50,200))
pygame.display.update()
pygame.time.delay(100)
