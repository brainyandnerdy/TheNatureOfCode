# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd

width = 800
height = 200
window = pygame.display.set_mode((width,height))

# Values taken from https://github.com/sol-prog/Perlin_Noise/blob/master/PerlinNoise.cpp
Gradient = [151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,
            8,99,37,240,21,10,23,190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,
            35,11,32,57,177,33,88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,
            134,139,48,27,166,77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,
            55,46,245,40,244,102,143,54, 65,25,63,161,1,216,80,73,209,76,132,187,208, 89,
            18,169,200,196,135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,
            250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,
            189,28,42,223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 
            43,172,9,129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,
            97,228,251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,
            107,49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
            138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]

class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A random walker object!
class Walker:

    def __init__(self, position, noff):
        self.position = position
        self.noff = noff
        
    def render(self):
        global window
        
        pygame.draw.ellipse(window, pygame.Color('white'), (self.position.x, self.position.y, 48, 48))  
        pygame.display.update()

    # Randomly move up, down, left, right, or stay in one place
    def step(self):
        global width
        global height
        
        # map(float value, float istart, float istop, float ostart, float ostop) {
        #        return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
        #    }
        # So the line:
        # self.position.x = map(perlin_noise(self.noff.x, 0), 0, 1, 0, width)
        # will become:
        # self.position.x = 0 + (width - 0) * ((perlin_noise(self.noff.x, 0) - 0) / (1 - 0))
        self.position.x = width * perlin_noise(self.noff.x, 0)
        self.position.y = height * perlin_noise(self.noff.y, 0)
        self.noff.x += 0.01
        self.noff.y += 0.01


# The Perlin noise implementation follows the C example from Wikipedia:
# https://en.wikipedia.org/wiki/Perlin_noise
def lerp(a0, a1, w):
    """
    * Function to linearly interpolate between a0 and a1
    * Weight w should be in the range [0.0, 1.0]
    *
    * as an alternative, this equivalent function (macro) can be used:
    * #define lerp(a0, a1, w) ((a0) + (w)*((a1) - (a0))) 
    """
    return (1.0 - w)*a0 + w*a1


def dotGridGradient(ix, iy, x, y):
    """
    Computes the dot product of the distance and gradient vectors.
    """
    # Precomputed (or otherwise) gradient vectors at each grid node
    global Gradient 

    # Compute the distance vector
    dx = x - ix
    dy = y - iy

    # Compute the dot-product
    return (dx*Gradient[(iy + ix) % len(Gradient)] + dy*Gradient[(iy + ix) % len(Gradient)])


def perlin_noise(x, y):
    """
    Compute Perlin noise at coordinates x, y
    """
    # Determine grid cell coordinates
    x0 = int(x)
    x1 = x0 + 1
    y0 = int(y)
    y1 = y0 + 1

    # Determine interpolation weights
    # Could also use higher order polynomial/s-curve here
    sx = x - float(x0)
    sy = y - float(y0)

    # Interpolate between grid point gradients
    n0 = dotGridGradient(x0, y0, x, y)
    n1 = dotGridGradient(x1, y0, x, y)
    ix0 = lerp(n0, n1, sx)

    n0 = dotGridGradient(x0, y1, x, y)
    n1 = dotGridGradient(x1, y1, x, y)
    ix1 = lerp(n0, n1, sx)

    value = lerp(ix0, ix1, sy)
    return value


w = Walker(PVector(width/2, height/2), PVector(rnd.randint(0,1000), rnd.randint(0,1000)))

def draw():
    global w

    w.step()
    w.render()

while(True):
  draw()
