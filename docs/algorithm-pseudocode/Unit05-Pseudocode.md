# Unit 05 - Basic Traversal and Search: Algorithm Pseudocode

## 1. Binary Tree Creation

```text
CREATE a Node class with data, left, and right

CREATE root node with value 1

CREATE left child of root with value 2
CREATE right child of root with value 3

CREATE left child of node 2 with value 4
CREATE right child of node 2 with value 5

DISPLAY the tree node information
```

---

## 2. Preorder Traversal

```text
FUNCTION Preorder(root)

    IF root is not NULL THEN
        DISPLAY root.data
        CALL Preorder(root.left)
        CALL Preorder(root.right)
    END IF

END FUNCTION
```

**Traversal Order: Root → Left → Right**

---

## 3. Inorder Traversal

```text
FUNCTION Inorder(root)

    IF root is not NULL THEN
        CALL Inorder(root.left)
        DISPLAY root.data
        CALL Inorder(root.right)
    END IF

END FUNCTION
```

**Traversal Order: Left → Root → Right**

---

## 4. Postorder Traversal

```text
FUNCTION Postorder(root)

    IF root is not NULL THEN
        CALL Postorder(root.left)
        CALL Postorder(root.right)
        DISPLAY root.data
    END IF

END FUNCTION
```

**Traversal Order: Left → Right → Root**

---

## 5. Recursive Tree Traversal

```text
CREATE a binary tree

CALL Preorder(root)
    DISPLAY Root
    CALL left subtree
    CALL right subtree

CALL Inorder(root)
    CALL left subtree
    DISPLAY Root
    CALL right subtree

CALL Postorder(root)
    CALL left subtree
    CALL right subtree
    DISPLAY Root
```

---

## 6. Iterative Tree Traversal

### Iterative Preorder

```text
CREATE a stack and push root

WHILE stack is not empty
    POP a node
    DISPLAY node data

    PUSH right child if it exists
    PUSH left child if it exists
END WHILE
```

### Iterative Inorder

```text
CREATE an empty stack
SET current = root

WHILE stack is not empty OR current is not NULL
    WHILE current is not NULL
        PUSH current into stack
        MOVE current to left child
    END WHILE

    POP node from stack
    DISPLAY node data
    MOVE current to right child
END WHILE
```

### Iterative Postorder

```text
CREATE stack1 and stack2
PUSH root into stack1

WHILE stack1 is not empty
    POP node from stack1
    PUSH node into stack2

    PUSH left child into stack1 if it exists
    PUSH right child into stack1 if it exists
END WHILE

WHILE stack2 is not empty
    POP and DISPLAY node data
END WHILE
```

---

## 7. Graph Using Adjacency Matrix

```text
SET number of vertices

CREATE a matrix of size vertices × vertices
INITIALIZE all values to 0

FUNCTION AddEdge(source, destination)
    SET matrix[source][destination] = 1
    SET matrix[destination][source] = 1
END FUNCTION

ADD all required edges

DISPLAY the adjacency matrix
```

---

# Conclusion

This document contains the pseudocode for the tree traversal and graph representation algorithms implemented in Unit 05.