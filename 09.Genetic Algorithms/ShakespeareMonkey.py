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

import time
import Population as pop

target = ""
popmax = 0
mutationRate = 0.0
population = None
t0 = time.time()

def setup():
    global target
    global popmax
    global mutationRate
    global population

    target = "To be or not to be."
    popmax = 200
    mutationRate = 0.01

    # Create a population with a target phrase, mutation rate, and population max
    population = pop.Population(target, mutationRate, popmax)

def draw():
    global population
    global t0
    
    while(1 == 1):
      # Generate mating pool
      population.naturalSelection()

      # Create next generation
      population.generate()

      # Calculate fitness
      population.calcFitness()
      displayInfo()

      # If we found the target phrase, stop
      if (population.isFinished() == True):
          print(str(time.time() - t0))
          break

def displayInfo():    
    """Display current status of population"""
    global population
    global popmax

    answer = population.getBest()
  
    print("Best phrase:" + str(answer) + "\n")
    print("total generations:     " + str(population.getGenerations()) + "\n")
    print("average fitness:       " + str(population.getAverageFitness()) + "\n")
    print("total population: " + str(popmax) + "\n")
    print("mutation rate:         " + str(int(mutationRate * 100)) + "%" + "\n")
    print("All phrases:\n" + str(population.allPhrases()) + "\n")

setup()
draw()


