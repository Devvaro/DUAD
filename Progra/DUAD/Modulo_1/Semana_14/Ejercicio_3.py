class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def  __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)

        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def pre_order(self, node):
        
        if node is not None:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)



tree= BinaryTree()
tree.insert("first")
tree.insert("second")
tree.insert("third")
tree.insert("forth")
tree.insert("fifth")
tree.insert("sixth")
tree.insert("seventh")

print("Pre order")
tree.pre_order(tree.root)