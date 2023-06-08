from GBFS import GreedyBFS
import time

start_time = time.time()

gbfs = GreedyBFS('arad','bucharest')
node = gbfs.search()

gbfs.printPath(node)

print("time : " + str(time.time() - start_time))