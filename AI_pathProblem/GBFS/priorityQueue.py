class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self,dict):
        self.queue.append(dict)

    def pop(self):
        try:
            if not self.isEmpty():
                max_val = 0
                for i in range(len(self.queue)):
                    if self.queue[i].h < self.queue[max_val].h:
                        max_val = i
                item = self.queue[max_val]
                del self.queue[max_val]
                return item
            else :
                return
        except IndexError:
            return

    def print(self):
        for i in self.queue:
            print(i)