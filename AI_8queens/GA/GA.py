import random
from Node import Node
class GeneticAlgorithm:

    def __init__(self,population_size,mutation_rate,max_generations,numberOfParent,numOffspring):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations =max_generations
        self.numberOfParent = numberOfParent
        self.numOffspring = numOffspring
        self.bestValues = 10000000000


    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            node = Node(random.sample(range(8), 8))
            self.population.append(node)

    def getSumOfFitness(self):
        sum = 0
        for gen in self.population:
            sum += gen.value
        return sum

    def evaluate_fitness(self):
        sum = self.getSumOfFitness()
        for gen in self.population :
            gen.setP(int(gen.value / sum * 100))

    def selection(self):

        fitness_values = []
        for get in self.population:
            fitness_values.append(get.P)
        parent = []

        for _ in range(self.numberOfParent):
            minFitness = min(fitness_values)
            index = fitness_values.index(minFitness)
            parent.append(self.population[index])
            fitness_values[index] = float('inf')

        return parent
    def crossover(self,parents):
        offspring = []
        for _ in range(self.numOffspring):
            parent1, parent2 = random.sample(parents, 2)
            crossoverPoint = random.randint(1, 6)
            child1State = parent1.state[:crossoverPoint] + parent2.state[crossoverPoint:]
            child2State = parent1.state[crossoverPoint:] + parent2.state[:crossoverPoint]
            child1 = Node(child1State)
            child2 = Node(child2State)
            offspring.append(child1)
            offspring.append(child2)

        return offspring

    def mutation(self,offspring):
        mutated_offspring = []
        for child in offspring:
            if random.random() > self.mutation_rate:
                mutation_point = random.randint(0, 7)
                child.state[mutation_point] = random.randint(0, 7)
            mutated_offspring.append(child)
        return mutated_offspring

    def printGeneration(self,population,NGeneration):
        print(str(NGeneration)+"'th generation:")
        print("[",end="")

        for gen in population :
            print("{ value : " + str(gen.value)+" , P : "+str(gen.P)+" ,state : "+str(gen.state)+"},",end="")
        print("]")
    def checkForBestSolve(self):
        for gen in self.population :
            if gen.value == 0 :
                return gen
            else:
                return False

    def saveBestSol(self,NGeneration):
        for gen in self.population :
            if (gen.value < self.bestValues):
                self.bestValues = gen.value
                self.bestSolGen = gen
                self.bestSolGeneration = NGeneration
    def ga(self):
        self.initialize_population()

        #sol = Node([3,7,0,4,6,1,5,2])
        #self.population[0] = sol

        flag = True
        generationNumber = 0
        initPopulation = self.population
        while generationNumber != self.max_generations:
            self.evaluate_fitness()
            result = self.checkForBestSolve()

            if(result != False):
                print("-------solution is found---------")
                print("state : " + str(result.state))
                self.printGeneration(self.population, generationNumber)
                flag = False
                break

            self.saveBestSol(generationNumber)

            self.printGeneration(self.population,generationNumber)
            parent = self.selection()
            newPopulation = []
            for _ in range(0 , int(self.numberOfParent / 2)):
                offspring = self.crossover(parent)
                mutated_offspring = self.mutation(offspring)
                child1 = mutated_offspring[0]
                child2 = mutated_offspring[1]
                newPopulation.append(child1)
                newPopulation.append(child2)

            self.population = newPopulation
            generationNumber += 1
        if flag :
            print("initial state : ")
            self.printGeneration(initPopulation,0)
            print("cant find awnser but best solution have P : "+str(self.bestSolGen.P)+" and value : "+str(self.bestSolGen.value)+" and states : "+str(self.bestSolGen.state)+" and find in "+str(self.bestSolGeneration)+" 'th generation")


