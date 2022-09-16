from math import sqrt
import random, operator

#CREATE THE FIRST POPULATION WITH COMPLETLY RANDOM CROMOSOMES
def initiatePopulation(populationSize, noOfCities):
    population = []

    for i in range(0, populationSize):
        cromosone = []
        for j in range(1, noOfCities):
            cromosone.append(j)
        random.shuffle(cromosone)

        cromosone.append(0)
        cromosone.insert(0, 0)
        population.append(cromosone)
    return population

#CALCULATE THE DISTANCE BETWEEN TWO CITIES
def fitness(cromosone, cityList):
    totalDistance = 0

    for i in range(0, len(cromosone) - 1):
        startCity = cityList[cromosone[i]]
        destinationCity = cityList[cromosone[i + 1]]
        
        xDistance = destinationCity[0] - startCity[0]
        yDistance = destinationCity[1] - startCity[1]

        distance = sqrt(pow(xDistance, 2) + pow(yDistance, 2))       
        totalDistance += distance
    return totalDistance

#MUTATION, SWAP TWO RANDOM GENES IN A CROMOSOME
def mutation(cromosome):
    a = random.randrange(1, len(cromosome) - 1)
    b = random.randrange(1, len(cromosome) - 1)

    while a != b:
        b = random.randrange(1, len(cromosome) - 1)
    temp = cromosome[a]
    cromosome[a] = cromosome[b]
    cromosome[b] = temp
    return cromosome

#SELECTS A RANDOM INDEX AND A RANDOM CROSSOVER SIZE TO PERFORM A CROSSOVER
#START AT THE INDEX, AND SELECT CrossoverSize NUMBER OF GENES FOR THE CROSSOVER FROM THE MOTHER
#CREATE A COPY Of THE FATHER AS CHILD
#REMOVE REMOVE THE SELECTED GENES FROM THE CHILD, SHUFFLE THE SELECTED GENES AND APPEND THE SELECTED GENES TO THE CHILD AGAIN
#A NEW CHILD HAS BEEN CREATED
def crossover(mother, father):
    crossoverSize = random.randrange(2, 5)
    index = random.randrange(1, len(mother) - 1 - crossoverSize)
    selectedGenes = []
    child = []

    for i in range(0, len(father)):
        child.append(father[i])

    for i in range(index, index + crossoverSize):
        selectedGenes.append(mother[i])

    for i in range(0, len(father)):
        for j in range(0, len(selectedGenes)):
            if father[i] == selectedGenes[j]:
                child.remove(selectedGenes[j])

    del child[len(child) - 1]
    random.shuffle(selectedGenes)

    for i in range(0, len(selectedGenes)):
        child.append(selectedGenes[i])
    child.append(0)  
    return child  


def createNewGeneration(previousGeneration):
    newGeneration = []
    


noOfCities = 15
noOfGenerations = 10
popSize = 20
cities = []
progress = []

for i in range(0, noOfCities):
    xCord = int(random.random() * 2000)
    yCord = int(random.random() * 2000)
    cities.append((xCord, yCord))

population = initiatePopulation(popSize, noOfCities)

for i in range(0, noOfGenerations):
    rankedPopulation = []
    for j in range(0, len(population)):
        distance = fitness(population[j], cities)
        rankedCromosome = {
            "distance": distance,
            "cromosome": population[j]
        }
        rankedPopulation.append(rankedCromosome)
    rankedPopulation = sorted(rankedPopulation, key = lambda d: d['distance'], reverse=False)
    progress.append(rankedPopulation[0])