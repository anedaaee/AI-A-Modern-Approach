from Node import Node
import queue
import numpy as np
import copy

class DepthLimitedSearch:

    def __init__(self, initStateArray,limit):

        self.goalStateArray = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.frontire = queue.LifoQueue()
        self.limit = limit
        self.initState = Node(initStateArray, None, 0, 1)
        self.numberOfNode = 1
        self.frontire.put(self.initState)

    def search(self):
        while not self.frontire.empty():
            node = self.frontire.get()
            if self.checkIfNodeIsGoal(node):

                 return  node

            if node.level > self.limit :
                cut_off = True
            else :
                Expend = self.Expand(node)
                for child in Expend :
                    self.frontire.put(child)

        if(cut_off):
            print("cant find Awnser")
            return


    def Expand(self, parent):
        Expand = []

        for i in range(0, 3):
            for j in range(0, 3):
                array = copy.deepcopy(parent.state)
                if (i - 1 >= 0):
                    array1 = copy.deepcopy(array)
                    temp = array1[i, j]
                    array1[i, j] = array1[i - 1, j]
                    array1[i - 1, j] = temp
                    self.numberOfNode += 1
                    child1 = Node(array1, parent, parent.level + 1, self.numberOfNode)
                    Expand.append(child1)
                if (i + 1 < 3):
                    array2 = copy.deepcopy(array)
                    temp = array2[i, j]
                    array2[i, j] = array2[i + 1, j]
                    array2[i + 1, j] = temp
                    self.numberOfNode += 1
                    child2 = Node(array2, parent, parent.level + 1, self.numberOfNode)
                    Expand.append(child2)
                if (j - 1 >= 0):
                    array3 = copy.deepcopy(array)
                    temp = array3[i, j]
                    array3[i, j] = array3[i, j - 1]
                    array3[i, j - 1] = temp
                    self.numberOfNode += 1
                    child3 = Node(array3, parent, parent.level + 1, self.numberOfNode)
                    Expand.append(child3)
                if (j + 1 < 3):
                    array4 = copy.deepcopy(array)
                    temp = array4[i, j]
                    array4[i, j] = array4[i, j + 1]
                    array4[i, j + 1] = temp
                    self.numberOfNode += 1
                    child4 = Node(array4, parent, parent.level + 1, self.numberOfNode)
                    Expand.append(child4)

        return Expand

    def printPath(self, node):
        path = []
        print("level: " + str(node.level))
        while True:

            if node:
                path.insert(0, node.state)

                if (node.parent):
                    node = node.parent
                else:
                    break

            else:
                break

        for p in path:
            print(p)

    def checkIfNodeIsGoal(self, node):
        flag = True
        for i in range(0, 3):
            for j in range(0, 3):
                if node.state[i, j] != self.goalStateArray[i, j]:
                    flag = False
        return flag