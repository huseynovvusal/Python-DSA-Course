class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
#
# node1.next = node2
# node2.next = node3
#
# print(node1.value)
# print(node1.next.value)
# print(node1.next.next.value)

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, new_node):
        current = self.head

        if(current):
            while(current.next):
                current = current.next

            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        current = self.head

        if(current.value == value):
            self.head = current.next
        else:
            prev = None

            while(current):
                if(current.value == value): break

                prev = current
                current = current.next

            if(current == None): return None

            prev.next = current.next


    def print(self):
        current = self.head

        while(current):
            print(current.value, end=" -> ")

            current = current.next

        print(None)


ll = LinkedList()

ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))

ll.delete(10)
ll.delete(40)

ll.print()