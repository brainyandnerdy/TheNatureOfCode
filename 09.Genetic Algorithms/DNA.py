# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Genetic Algorithm, Evolving Shakespeare

# A class to describe a psuedo-DNA, i.e. genotype
#   Here, a virtual organism's DNA is an array of character.
#   Functionality:
#      -- convert DNA into a string
#      -- calculate DNA's "fitness"
#      -- mate DNA with another set of DNA
#      -- mutate DNA

import random
import math

class DNA:    
    def __init__(self, num):
        """Constructor (makes a random DNA)""" 
        self.genes = ["x"] * num # The genetic sequence as a string
        self.fitness = 0.0

        for i in range(0,len(self.genes)):
            self.genes[i] = chr(random.randint(32,128)) # Pick from range of chars given by an ASCII number

    def getPhrase(self):        
        return "".join(self.genes)
    
    def calcFitness(self, target):
        """Fitness function (returns floating point % of "correct" characters)"""
        score = 0
        for i in range(0, len(self.genes)):
            if(self.genes[i] == target[i]):
                score += 1
        # fancy fitness version:
        #self.fitness = math.pow(2, score)
        self.fitness = score / len(target)

    def crossover(self, partner):
        """Crossover"""
        child = DNA(len(self.genes)) # A new child

        midpoint = random.randint(0,len(self.genes)-1) # Pick a midpoint

        # Half from one, half from the other
        for i in range(0,len(self.genes)):
            if(i > midpoint):
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutationRate):
        """Based on a mutation probability, picks a new random character"""
        for i in range(0, len(self.genes)):
            if(random.random() < mutationRate):
                self.genes[i] = chr(random.randint(32,128))

