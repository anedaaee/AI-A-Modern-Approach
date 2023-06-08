from database import request
from Node import Node
import queue
import json
class DepthLimitedSearch:

    def __init__(self,initStateName , goalStateName , limit):

        self.goalStateName = goalStateName
        self.numberOfNode = 0
        self.frontire = queue.LifoQueue()
        self.limit = limit

        result = request(f"select * from citys where name = '{initStateName}';")

        if len ( result ) > 0 :
            self.initState = Node(None,result[0]["name"] , json.loads(result[0]["paths"])["paths"],0,self.numberOfNode)
            self.frontire.put(self.initState)

        else:
            print('error happend')

    def search(self):
        try :
            while not self.frontire.empty():

                node = self.frontire.get()


                if node.name == self.goalStateName :
                     return  node

                if node.level > self.limit :
                    result = 'cut-off'
                elif node.level == self.limit :
                    #self.frontire.get()
                    continue
                else :
                    Expend = self.expand(node)
                    if not Expend :
                        raise Exception('error happend in expend')

                    for child in Expend :
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
                    newNode = Node(parent, DBNode[0]["name"], json.loads(DBNode[0]["paths"])["paths"], parent.level + 1,self.numberOfNode)
                    Expend.append(newNode)

                else:
                    raise Exception('cant find city')

            return Expend
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
