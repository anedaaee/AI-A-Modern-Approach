import copy
from Node import Node
import queue
import numpy as np
from priorityQueue import PriorityQueue
class GreadyBreadthFirstSearch:
        def __init__(self,initStateArray ):

                self.goalStateArray = np.array([[0,1,2],[3,4,5],[6,7,8]])

                self.frontire = PriorityQueue()
                self.reached = []

                self.initState = Node(initStateArray,None,0,2)
                self.numberOfNode = 1
                print(self.initState.h)
                self.frontire.insert(self.initState)
                self.reached.append(self.initState)

        def search(self):

                while not self.frontire.isEmpty() :

                        node = self.frontire.pop()
                        if self.checkIfNodeIsGoal(node):
                                return node

                        expend = self.Expend(node)

                        if expend :
                                for child in expend:
                                        if self.checkIfNodeIsGoal(child):
                                                return child

                                        self.frontire.insert(child)
                                        self.reached.append(child)





        def Expend(self,parent):
                Expand = []

                for i in range(0,3):
                        for j in range(0, 3):
                                array = copy.deepcopy(parent.state)
                                if( i - 1 >= 0):
                                        array1 = copy.deepcopy(array)
                                        temp = array1[i,j]
                                        array1[i,j] = array1[i-1,j]
                                        array1[i-1,j] = temp
                                        self.numberOfNode += 1
                                        child1 = Node(array1,parent,parent.level+1,self.numberOfNode)
                                        Expand.append(child1)
                                if(i + 1 < 3):
                                        array2 = copy.deepcopy(array)
                                        temp = array2[i,j]
                                        array2[i,j] = array2[i+1,j]
                                        array2[i+1,j] = temp
                                        self.numberOfNode += 1
                                        child2 = Node(array2, parent, parent.level + 1, self.numberOfNode)
                                        Expand.append(child2)
                                if (j - 1 >= 0):
                                        array3 = copy.deepcopy(array)
                                        temp = array3[i,j]
                                        array3[i,j] = array3[i,j-1]
                                        array3[i,j - 1] = temp
                                        self.numberOfNode += 1
                                        child3 = Node(array3, parent, parent.level + 1, self.numberOfNode)
                                        Expand.append(child3)
                                if (j + 1 < 3):
                                        array4 = copy.deepcopy(array)
                                        temp = array4[i,j]
                                        array4[i,j] = array4[i,j + 1]
                                        array4[i,j + 1] = temp
                                        self.numberOfNode += 1
                                        child4 = Node(array4, parent, parent.level + 1, self.numberOfNode)
                                        Expand.append(child4)

                return Expand

        def printPath(self,node):
                path = []
                print("level: "+str(node.level))
                while True :
                        if node :
                                path.insert(0,node.state)
                                print(node.state)
                                print("h: "+str(node.h))
                                if(node.parent):

                                        node = node.parent
                                else:
                                        break

                        else:
                                break

                #for p in path :
                        #print(p)

        def checkIfNodeIsGoal(self,node):
                flag = True
                for i in range(0,3):
                        for j in range(0,3):
                                if node.state[i,j] != self.goalStateArray[i,j]:
                                        flag = False
                return flag

        def equal(self,node1,node2):
                flag = True
                for i in range(0,3):
                        for j in range(0,3):
                                if node1.state[i,j] != node2.state[i,j]:
                                        flag = False
                return flag