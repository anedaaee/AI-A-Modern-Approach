from DLS import DepthLimitedSearch
import  time
import numpy as np

start_time = time.time()


dls = DepthLimitedSearch( np.array([[0,4,2],[3,1,5],[7,8,6]]),5)
node = dls.search()
dls.printPath(node)

print("time : "+str(time.time() - start_time))