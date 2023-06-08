from DLSAStar import DepthLimitedSearchAStar
from database import request
class IterativeDeepeningSearchAStar:

    def __init__(self, initStateName ,goalStateName ):
        self.initStateName = initStateName
        self.goalStateName = goalStateName

    def Search (self) :
#        h = request(f"select value from heuristic_for_city_prob where dest='{self.goalStateName}' and start='{self.initStateName}';")
#        h = h[0]["value"]
        h=0
        while True :
            #print(h)
            self.dlsAStar = DepthLimitedSearchAStar(self.initStateName,self.goalStateName,h)
            node = self.dlsAStar.search();
            if node :
                self.dlsAStar.printPath(node)
                print(node.nodeNumber)
                break
            h += 20
