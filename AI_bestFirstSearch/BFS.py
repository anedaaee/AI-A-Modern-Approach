from Node import Node
from priorityQueue import PriorityQueue
import database
import json


# print(json.loads(result[0]["paths"])["paths"][0])

class BFS:
    def __init__(self, initialState,goalState):
        result = database.request(f"select * from citys where name = '{initialState}';")
        if (len(result) > 0):
            self.initialState = Node(None, result[0]["name"], json.loads(result[0]["paths"])["paths"], 0)
            self.goalState = goalState
            self.frontier = PriorityQueue()
            self.frontier.insert(self.initialState)
            self.reached = []
        else:
            return
    def search(self):
        while self.frontier.isEmpty() != True :
            node = self.frontier.delete()
            if (node.name == self.goalState):
                return node

            else:
                expand = self.expand(node)
                flag = True
                for child in expand:
                    if(child in self.reached):
                        if(child.path_cost < self.reached[self.reached.index(child)]):
                            self.frontier.insert(child)
                            self.reached.remove(self.reached.index(child))
                            self.reached.append(child)
                            flag = False
                        else :
                            flag = False
                    if flag == True :
                        self.frontier.insert(child)
                        self.reached.append(child)
        return False



    def expand(self,node):
        s = node.name
        for child in node.childs:
            result = database.request(f"select * from citys where name = '{child}';")

            if(len(result) > 0):
                newNode = Node(node.name , result[0]["name"], json.loads(result[0]["paths"])["paths"] , node.path_cost )
                pathCost = database.request(f"select cost from path_cost where (city1 = '{node.name}' and city2 = '{newNode.name}') or (city1 = '{newNode.name}' and city2 = '{node.name}');")
                newNode.path_cost += pathCost
                expand = []
                expand.append(newNode)
                return expand
            else:
                return False


