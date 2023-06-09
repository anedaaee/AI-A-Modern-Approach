from BFS import BreadthFirstSearch
import  time
import numpy as np

start_time = time.time()


bfs = BreadthFirstSearch( np.array([[0,4,2],[3,1,5],[7,8,6]]))
node = bfs.search()
bfs.printPath(node)

print("time : "+str(time.time() - start_time))