class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_node):
        current = self.head

        if(current):
            while(current.next):
                current = current.next

            current.next = new_node
            current.next.prev = current
        else:
            self.head = new_node

    def delete(self, value):
        current = self.head

        if(current.value == value):
            self.head = current.next
            if(self.head): self.head.prev = None
        else:
            prev = None

            while(current):
                if(current.value == value): break

                prev = current
                current = current.next

            if(current == None): return None

            prev.next = current.next
            if(current.next): prev.next.prev = prev


    def print(self):
        current = self.head

        while(current):
            prev = None if not current.prev else current.prev.value
            next = None if not current.next else current.next.value

            print((prev, current.value, next), end = " <-> ")

            current = current.next

        print(None)


ll = LinkedList()

ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))

ll.delete(30)
ll.delete(10)

ll.print()