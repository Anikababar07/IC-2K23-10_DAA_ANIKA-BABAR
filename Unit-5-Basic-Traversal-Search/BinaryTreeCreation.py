# Binary Tree Creation

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating the binary tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


# Displaying the created tree
print("Binary Tree Created Successfully!")
print("Root:", root.data)
print("Left Child of Root:", root.left.data)
print("Right Child of Root:", root.right.data)
print("Left Child of Node 2:", root.left.left.data)
print("Right Child of Node 2:", root.left.right.data)