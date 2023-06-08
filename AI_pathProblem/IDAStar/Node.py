class Node :
    def __init__(self,parent,name,childs,h,pathCost,nodeNumber):
        self.parent = parent
        self.name = name
        self.childs = childs
        self.h = h
        self.nodeNumber = nodeNumber
        self.pathCost = pathCost
    def __str__(self):
        return f"name={self.name},childs={self.childs},pathCost={self.level},numberOfNode={self.nodeNumber},parent={self.parent}"

