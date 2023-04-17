from DLS import DepthLimitedSearch
import time

start_time = time.time()

dls = DepthLimitedSearch('rimnicu vilcea','fagaras',2)
node = dls.search()
if node :
    dls.printPath(node)
if node == 'cut-off':
    print('cut-off')

print("time : " + str(time.time() - start_time))