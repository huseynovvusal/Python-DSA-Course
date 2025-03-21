class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if(self.isEmpty()):
            return None

        return self.stack[-1]

    def __str__(self):
        return "[" + ", ".join(map(str, self.stack)) + "]"


stack = Stack()

stack.push(10)
stack.push(15)
stack.push(20)

print(stack)

stack.pop()
stack.pop()

print(stack.peek())

stack.pop()

print(stack.isEmpty())