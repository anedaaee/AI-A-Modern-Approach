class Node :
    def __init__(self,parent,name,childs,level,nodeNumber):
        self.parent = parent
        self.name = name
        self.childs = childs
        self.level = level
        self.nodeNumber = nodeNumber
    def __str__(self):
        return f"name={self.name},childs={self.childs},pathCost={self.level},numberOfNode={self.nodeNumber},parent={self.parent}"

