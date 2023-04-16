class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self,dict):
        self.queue.append(dict)

    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                print(self.queue[i])
                if self.queue[i]["path_cost"] > self.queue[max_val]["path_cost"]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            return
