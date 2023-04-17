from DLS import DepthLimitedSearch
class IterativeDeepeningSearch:

    def __init__(self, initStateName ,goalStateName ):
        self.initStateName = initStateName
        self.goalStateName = goalStateName

    def Search (self) :
        i = 0
        while True :
            self.dls = DepthLimitedSearch(self.initStateName,self.goalStateName,i)
            node = self.dls.search();
            if node :
                self.dls.printPath(node)
                print(node.level)
                break
            i += 1