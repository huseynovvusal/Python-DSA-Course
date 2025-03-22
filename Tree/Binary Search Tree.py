class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if(not self.root):
            self.root = new_node
            return

        current = self.root

        while(current):
            if(value < current.value):
                if(current.left is None):
                    current.left = new_node
                    return

                current = current.left

            elif(value > current.value):
                if(current.right is None):
                    current.right = new_node
                    return

                current = current.right

    def inorder(self, node):
        if(not node): return

        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

bst = BST()

bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(25)

bst.inorder(bst.root)