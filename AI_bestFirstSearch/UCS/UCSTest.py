from UCS import UniformCasrSearch
import time

start_time = time.time()

ucs = UniformCasrSearch('arad','bucharest')
node = ucs.search()

ucs.printPath(node)

print("time : " + str(time.time() - start_time))