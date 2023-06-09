from DLS import DepthLimitedSearch
class IterativeDeepeningSearch:

    def __init__(self, initStateName  ):
        self.initStateName = initStateName

    def Search (self) :
        i = 0
        while True :
            self.dls = DepthLimitedSearch(self.initStateName,i)
            node = self.dls.search();
            if node :
                self.dls.printPath(node)
                break
            i += 1