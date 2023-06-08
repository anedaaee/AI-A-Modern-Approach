class Node :
    def __init__(self,parent,name,childs,path_cost,h,nodeNumber):
        self.parent = parent
        self.name = name
        self.childs = childs
        self.path_cost = path_cost
        self.h = h
        self.nodeNumber = nodeNumber
    def __str__(self):
        return f"name={self.name},childs={self.childs},pathCost={self.path_cost},numberOfNode={self.nodeNumber},parent={self.parent}"

