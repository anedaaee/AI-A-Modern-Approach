class Node :
    def __init__(self,parent,name,childs,path_cost):
        self.parent = parent
        self.name = name
        self.childs = childs
        self.path_cost = path_cost

    def __str__(self) -> str:
        return f"{self.name},{self.childs},{self.path_cost}"

