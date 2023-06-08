from database import request
from Node import Node
import queue
import json
class DepthLimitedSearchAStar:

    def __init__(self,initStateName , goalStateName , limit):

        self.goalStateName = goalStateName
        self.numberOfNode = 0
        self.frontire = queue.LifoQueue()
        self.limit = limit

        result = request(f"select * from citys where name = '{initStateName}';")

        if len ( result ) > 0 :
            self.initState = Node(None,result[0]["name"] , json.loads(result[0]["paths"])["paths"],0,0,self.numberOfNode)
            self.frontire.put(self.initState)

        else:
            print('error happend')

    def search(self):
        try :
            while not self.frontire.empty():

                node = self.frontire.get()


                if node.name == self.goalStateName :
                     return  node
                print(self.limit)
                print(node.h + node.pathCost)
                print()
                if node.h + node.pathCost > self.limit :
                    result = 'cut-off'
                else :
                    Expend = self.expand(node)
                    if not Expend :
                        raise Exception('error happend in expend')

                    for child in Expend:
                        self.frontire.put(child)

        except Exception('error happend in expend'):
            print('error happend in expend')
            return

    def expand(self,parent):
        try:

            childs = parent.childs

            Expend = []
            for child in childs:

                DBNode = request(f"select * from citys where name = '{child}';")

                if len(DBNode) > 0:

                    self.numberOfNode += 1
                    newNode = Node(parent, DBNode[0]["name"], json.loads(DBNode[0]["paths"])["paths"], 0, 0, self.numberOfNode)
                    pathCost = request(f"select cost from path_cost where (city1 = '{parent.name}' and city2 = '{newNode.name}') or (city1 = '{newNode.name}' and city2 = '{parent.name}');")
                    h = request(f"select value from heuristic_for_city_prob where dest='{self.goalStateName}' and start='{newNode.name}';")



                    if pathCost and h:
                        newNode.patCost = parent.pathCost + pathCost[0]["cost"]
                        newNode.h = h[0]["value"]
                        Expend.append(newNode)

                    else:
                        raise Exception('heuristic err')

                else:
                    raise Exception('cant find city')

            return Expend
        except Exception('heuristic err'):
            return False

        except Exception('cant find city'):
            print('cant find city')
            return

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
