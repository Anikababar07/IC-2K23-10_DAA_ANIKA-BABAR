# Iterative Tree Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Iterative Preorder Traversal
def preorder_iterative(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


# Iterative Inorder Traversal
def inorder_iterative(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


# Iterative Postorder Traversal
def postorder_iterative(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        print(node.data, end=" ")


# Create Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Iterative Preorder Traversal:")
preorder_iterative(root)

print("\n\nIterative Inorder Traversal:")
inorder_iterative(root)

print("\n\nIterative Postorder Traversal:")
postorder_iterative(root)