# from collections import deque
#
# d = deque()
#
# d.append(10)
# d.append(20)
# d.appendleft(5)
#
# print(d.popleft())
from collections import deque


class Deque:
    def __init__(self):
        self.deque = []

    def addLeft(self,item):
        self.deque.insert(0,item)

    def addRight(self,item):
        self.deque.append(item)

    def removeLeft(self):
        return self.deque.pop(0)

    def removeRight(self):
        return self.deque.pop()

    def isEmpty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

    def __str__(self):
        return "[" + ", ".join(map(str, self.deque)) + "]"

d = Deque()

d.addRight(10)
d.addRight(20)
d.addLeft(30)

d.removeLeft()
d.removeRight()

print(d)
print(d.size())

d.removeRight()

print(d.isEmpty())