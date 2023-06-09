from GA import GeneticAlgorithm
import time
start_time = time.time()

ga = GeneticAlgorithm(8,10,1000,8,1)
ga.ga()

print("time : " + str(time.time() - start_time))
