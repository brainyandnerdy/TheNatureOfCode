# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import random as rnd
import os.path

width = 640
height = 360
window = pygame.display.set_mode((width,height))
window.fill((0,0,0))  # Fills the screen with black

# Simple Perceptron Example
# See: http://en.wikipedia.org/wiki/Perceptron
# Code based on text "Artificial Intelligence", George Luger

class Trainer:
    """ A class to describe a training point
        Has an x and y, a "bias" (1) and known output
        Could also add a variable for "guess" but not required here
    """
    def __init__(self, x, y, a):
        self.inputs = []
        self.inputs.append(x)
        self.inputs.append(y)
        self.inputs.append(1)
        self.answer = a

        
# Perceptron Class
class Perceptron:
    def __init__(self, n, c__):
        self.weights = [] # Array of weights for inputs
        for i in range(0, n):
            self.weights.append(rnd.uniform(-1, 1))
        self.c = c__ # learning constant
    

    def activate(self, sum):
        if sum > 0:
            return 1
        else:
            return -1

    
    def getWeights(self):
        return self.weights # Return weights


    def feedforward(self, inputs):
        """ Guess -1 or 1 based on input values """
        sum = 0 # Sum of all values
        for i in range(0, len(self.weights)):
            sum += inputs[i] * self.weights[i]

        # Result is sign of the sum, -1 or 1
        return self.activate(sum)


    def train(self, inputs, desired):
        """ Function to train the Perceptron
            Weights are adjusted based on "desired" answer """
        guess = self.feedforward(inputs) # Guess the result
        
        # Compute the factor for changing the weight based on the error
        # Error = desired output - guessed output
        # Note this can only be 0, -2, or 2
        # Multiply by learning constant
        error = desired - guess
        # Adjust weights based on weightChange * input
        for i in range(0, len(self.weights)):
            self.weights[i] += self.c * error * inputs[i]

# The function to describe a line
def f(x):
    return 2 * x + 1

# Setup
count = 0 # We will train the perceptron with one "Point" object at a time

# Coordinate space
xmin = -400
ymin = -100
xmax = 400
ymax = 100

training = [] # A list of points we will use to "train" the perceptron
# Create a random set of training points and calculate the "known" answer
for i in range(0, 2000):
    #x = rnd.randint(-width/2, width/2)
    #y = rnd.randint(-height/2, height/2)
    x = rnd.randint(0, width)
    y = rnd.randint(0, height)
    answer = 1
    if(y < f(x)):
        answer = -1
    training.append(Trainer(x, y, answer))

# A Perceptron object
# The perceptron has 3 inputs -- x, y, and bias
# Second value is "Learning Constant"
ptron = Perceptron(3, 0.01) 

def draw():
    global window
    global width
    global height
    global count 
    global training
    global ptron
    global xmin 
    global ymin 
    global xmax
    global ymax

    window.fill((0,0,0))  # Fills the screen with black

    # Draw the line
    x1 = xmin
    y1 = f(x1)
    x2 = xmax
    y2 = f(x2)
    pygame.draw.line(window, (255, 255, 255),(x1, y1), (x2, y2), 4)
    pygame.display.update() 

    # Draw the line based on the current weights
    # Formula is weights[0]*x + weights[1]*y + weights[2] = 0
    weights = ptron.getWeights()
    x1 = xmin
    y1 = (-weights[2] - weights[0]*x1)/weights[1]
    x2 = xmax
    y2 = (-weights[2] - weights[0]*x2)/weights[1]
    pygame.draw.line(window, (255, 255, 255),(x1, y1), (x2, y2), 1)

    pygame.display.update() 

    # Train the Perceptron with one "training" point at a time
    ptron.train(training[count].inputs, training[count].answer)
    count = (count + 1) % len(training)

    # Draw all the points based on what the Perceptron would "guess"
    # Does not use the "known" correct answer
    for i in range(0, count):
        guess = ptron.feedforward(training[i].inputs)
        if (guess > 0): 
            pygame.draw.ellipse(window, pygame.Color('red'), (training[i].inputs[0], training[i].inputs[1], 8, 8)) 
        else:
            pygame.draw.ellipse(window, pygame.Color('white'), (training[i].inputs[0], training[i].inputs[1], 8, 8)) 
        pygame.display.update() 

while (True):
    draw()