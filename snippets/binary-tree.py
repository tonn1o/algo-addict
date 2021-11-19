class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()

        print(self.data)

        if self.right:
            self.right.printInOrder()

    def traverseInOrder(self, node):
        res = []

        if node:
            res = self.traverseInOrder(node.left)
            res.append(node.data)
            res = res + self.traverseInOrder(node.right)

        return res

root = Node(10)
root.insert(9)
root.insert(8)
root.insert(11)
root.insert(12)
print(root.traverseInOrder(root)) # [8, 9, 10, 11, 12]

