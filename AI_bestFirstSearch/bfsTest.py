from BFS import BFS

bfs = BFS('arad',"bucharest")
result = bfs.search()
print(result)
if(result):
    while(result.parent):
        print(result)