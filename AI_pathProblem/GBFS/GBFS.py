import json
import database
from Node import Node
from priorityQueue import PriorityQueue
class GreedyBFS:

    def __init__(self,initStateName,goalStateName):

        self.goalStateName = goalStateName
        self.numberOfNode = 0
        self.frontier = PriorityQueue()
        self.reached = []

        result = database.request(f"select * from citys where name = '{initStateName}';")

        if len ( result ) > 0 :
            self.initState = Node(None,result[0]["name"] , json.loads(result[0]["paths"])["paths"],0,self.numberOfNode)
            self.frontier.insert(self.initState)
            self.reached.append(self.initState)
        else:
            print('error happend')

    def search(self):
        try:
            while not self.frontier.isEmpty():

                node = self.frontier.pop()

                if node.name == self.goalStateName :
                    return node

                Expend = self.expand(node)

                if Expend:
                    for child in Expend :
                        flag1 = True
                        flag2 = True
                        for reach in self.reached:
                            if child.name == reach.name :
                                flag1 = False
                                if child.h >= reach.h :
                                    flag2 = False
                        if flag1 :
                            self.frontier.insert(child)
                            self.reached.append(child)

                        elif  (not flag1) and flag2:
                            self.frontier.insert(child)

                            for reach in self.reached:

                                if child.name == reach.name :
                                    self.reached.remove(reach)
                                    self.reached.append(child)

                else:
                    raise Exception('error in expending')
                    return

            return False

        except Exception('error in expending'):
            print('error in expending')
            return
    def expand(self,parent):

        childs = parent.childs


        Expend = []
        try :
            for child in childs :

                DBNode = database.request(f"select * from citys where name = '{child}';")

                if len(DBNode) > 0 :
                    self.numberOfNode += 1

                    newNode = Node(parent , DBNode[0]["name"], json.loads( DBNode[0]["paths"] )["paths"] , 0 , self.numberOfNode )

                    h = database.request(f"select value from heuristic_for_city_prob where dest='{self.goalStateName}' and start='{newNode.name}';")

                    if h :
                        newNode.h =  h[0]["value"]
                        Expend.append(newNode)


                    else:
                        raise Exception('path cost err')

                else :
                    raise Exception('cant find node')

            return Expend
        except Exception('path cost err'):
            return False

        except Exception('cant find node'):
            return False

    def printPath(self,node):
        path = []
        while True :

            if node :
                path.insert(0,node.name)

                if(node.parent):
                    node = node.parent
                else:
                    break

            else:
                break

        print(path)
