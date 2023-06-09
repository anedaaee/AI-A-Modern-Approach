import numpy as np

class Node :
    def __init__(self,state,parent,level,nodeNumber):
        self.goalStateArray = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.state = state
        self.parent = parent
        self.level = level
        self.nodeNumber = nodeNumber
        self.h = self.huristic()

    def huristic(self):
        h = 0
        for i in range (0,3):
            for j in range(0, 3):
                x = self.state[i,j]
                for m in range(0, 3):
                    for n in range(0, 3):
                        if x == self.goalStateArray[m,n]:
                            h += abs(m-i) + abs(n-j)
                            break
        return h


    def __str__(self):
        return f"state={self.state},pathCost={self.level},numberOfNode={self.nodeNumber},parent={self.parent}"

