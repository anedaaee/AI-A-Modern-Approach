from AStar import AStar
import time

start_time = time.time()

aStar = AStar('arad','bucharest')
node = aStar.search()

aStar.printPath(node)

print("time : " + str(time.time() - start_time))