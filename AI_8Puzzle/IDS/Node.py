

class Node :
    def __init__(self,state,parent,level,nodeNumber):
        self.state = state
        self.parent = parent
        self.level = level
        self.nodeNumber = nodeNumber
    def __str__(self):
        return f"state={self.state},level={self.level},numberOfNode={self.nodeNumber},parent={self.parent}"

