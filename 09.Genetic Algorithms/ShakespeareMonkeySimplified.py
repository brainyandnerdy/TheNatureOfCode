# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Genetic Algorithm, Evolving Shakespeare

# Demonstration of using a genetic algorithm to perform a search

# setup()
  # Step 1: The Population 
    # Create an empty population (an array or ArrayList)
    # Fill it with DNA encoded objects (pick random values to start)

# draw()
  # Step 1: Selection 
    # Create an empty mating pool (an empty ArrayList)
    # For every member of the population, evaluate its fitness based on some criteria / function, 
      #and add it to the mating pool in a manner consistant with its fitness, i.e. the more fit it 
      #is the more times it appears in the mating pool, in order to be more likely picked for reproduction.

  # Step 2: Reproduction Create a new empty population
    # Fill the new population by executing the following steps:
       #1. Pick two "parent" objects from the mating pool.
       #2. Crossover -- create a "child" object by mating these two parents.
       #3. Mutation -- mutate the child's DNA based on a given probability.
       #4. Add the child object to the new population.
    # Replace the old population with the new population
  
   # Rinse and repeat
import DNA
import random as rd

mutationRate = 0.01         # Mutation rate
totalPopulation = 150       # Total Population

population = list()             # Array to hold the current population
target = ""                 # Target phrase

def Setup():
    global population
    global totalPopulation
    global target

    target = "to be or not to be"
    population = [DNA.DNA(len(target))] * totalPopulation # Create a totalPopulation number of DNA objects

    for i in range(0,len(population)):
        population[i] = DNA.DNA(len(target))
        

def Draw():
    global population
    global target
    global mutationRate

    for i in range(0,len(population)):
        population[i].calcFitness(target)

    matingPool = list()    # ArrayList which we will use for our "mating pool"

    for i in range(0,len(population)):
        nnnn = int(population[i].fitness * 100) # Arbitrary multiplier, we can also use monte carlo method
        for j in range(0, nnnn):                # and pick two random numbers
            matingPool.append(population[j])
    
    for i in range(0, len(population)):
        a = rd.randint(0,len(matingPool) - 1)
        b = rd.randint(0,len(matingPool) - 1)
        partnerA = matingPool[a]
        partnerB = matingPool[b]
        child = partnerA.crossover(partnerB)
        child.mutate(mutationRate)
        population[i] = child
    
    everything = ""

    for i in range(0, len(population)):
        everything += population[i].getPhrase() + "\n"
    print(everything)

Setup()
Draw()

