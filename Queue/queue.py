class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.insert(0, item)

    def dequeue(self):
        self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return "[" + ", ".join(map(str, self.queue)) + "]"

queue = Queue()

print(queue.isEmpty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.dequeue()

print(queue)

print(queue.size())