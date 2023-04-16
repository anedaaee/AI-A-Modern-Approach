from Node import Node
from database import request
import queue
import json
class BreadthFirstSearch:
        def __init__(self,initStateName , goalStateName):

                self.goalStateName = goalStateName
                self.numberOfNode = 0
                self.frontire = queue.Queue()
                self.reached = []

                result = request(f"select * from citys where name = '{initStateName}';")

                if len (result) > 0 :
                        self.initState = Node(None,result[0]["name"] ,json.loads(result[0]["paths"])["paths"],0,self.numberOfNode)
                        self.frontire.put(self.initState)
                        self.reached.append(self.initState)
                else:
                        return
                        print('error happend')

        def search(self):
                try:
                        while not self.frontire.empty() :

                                node = self.frontire.get()

                                if node.name == self.goalStateName :
                                        return node

                                expend = self.Expend(node)

                                if expend :
                                        for child in expend:
                                                if(child.name == self.goalStateName):
                                                        return child
                                                flag = True
                                                for reach in self.reached:
                                                        if child.name == reach.name:
                                                                flag = False
                                                if flag :
                                                        self.frontire.put(child)
                                                        self.reached.append(child)
                                else :
                                        raise Exception('error in expending')

                        return
                except Exception('error in expending'):
                        print('error in expending')
                        return


        def Expend(self,parent):
                try:

                        childs = parent.childs


                        Expend = []
                        for child in childs :

                                DBNode = request(f"select * from citys where name = '{child}';")

                                if len(DBNode) > 0 :

                                        self.numberOfNode += 1
                                        newNode = Node(parent, DBNode[0]["name"], json.loads(DBNode[0]["paths"])["paths"], parent.level + 1,self.numberOfNode)
                                        Expend.append(newNode)

                                else :
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