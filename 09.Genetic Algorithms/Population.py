# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Genetic Algorithm, Evolving Shakespeare

# A class to describe a population of virtual organisms
# In this case, each organism is just an instance of a DNA object

import random as rd
import DNA 

class Population:
    def __init__(self, p, m, num):
        self.mutationRate = m     # Mutation rate
        self.target = p             # Target phrase
        self.population = [DNA.DNA(len(self.target))] * num  # Array to hold the current population
        
        for i in range(0, len(self.population)):
            self.population[i] = DNA.DNA(len(self.target))
        
        self.calcFitness()
        self.matingPool = list()        # ArrayList which we will use for our "mating pool" 
        self.generations = 0           # Number of generations
        self.finished = False              # Are we finished evolving?
        self.perfectScore = 1

    def calcFitness(self):
        """Fill our fitness array with a value for every member of the population"""
        for i in range(0, len(self.population)):
            # The original line was population[i].fitness(target);
            self.population[i].calcFitness(self.target)
    
    def naturalSelection(self):
        """Generate a mating pool"""
        self.matingPool.clear()
        maxFitness = 0.0

        for i in range(0,len(self.population)):
            if(self.population[i].fitness > maxFitness):
                maxFitness = self.population[i].fitness

        # Based on fitness, each member will get added to the mating pool a certain number of times
        # a higher fitness = more entries to mating pool = more likely to be picked as a parent
        # a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
        for i in range(0, len(self.population)):
            #ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
            #float fitness = map(population[i].fitness,0,maxFitness,0,1);
            fitness = (self.population[i].fitness / maxFitness) 
            n = int(fitness * 100) # Arbitrary multiplier, we can also use monte carlo method
            for j in range(0,n):
                  self.matingPool.append(self.population[i])

    def generate(self):
        """Create a new generation"""
        # Refill the population with children from the mating pool
        for i in range(0, len(self.population)):
            a = rd.randint(0, len(self.matingPool) - 1)
            b = rd.randint(0, len(self.matingPool) - 1)
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            self.population[i] = child
        self.generations += 1
    
    def getBest(self):
        """Compute the current "most fit" member of the population"""
        worldrecord = 0.0
        index = 0
        for i in range(0, len(self.population)):
            if(self.population[i].fitness > worldrecord):
                index = i
                worldrecord = self.population[i].fitness
        
        if worldrecord == self.perfectScore:
            self.finished = True
        
        return self.population[index].getPhrase()

    def isFinished(self):
        return self.finished
    
    def getGenerations(self):
        return self.generations

    def getAverageFitness(self):
        """Compute average fitness for the population"""
        total = 0.0
        for i in range(0,len(self.population)):
            total += self.population[i].fitness
        return total / len(self.population)

    def allPhrases(self):
        everything = ""    
        displayLimit = min(len(self.population),50)
        for i in range(0,displayLimit):
            everything += self.population[i].getPhrase() + "\n"
    
        return everything
