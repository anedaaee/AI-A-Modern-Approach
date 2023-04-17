from BFS import BreadthFirstSearch
import  time
start_time = time.time()

bfs = BreadthFirstSearch('arad','bucharest')
node = bfs.search()
bfs.printPath(node)

print("time : "+str(time.time() - start_time))