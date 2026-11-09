# Unit 05 - Basic Traversal and Search: Algorithm Flowcharts

## 1. Binary Tree Creation

```mermaid
flowchart TD
    A([Start]) --> B[Create Root Node]
    B --> C[Create Left Child]
    C --> D[Create Right Child]
    D --> E[Create Remaining Child Nodes]
    E --> F[Display Tree Information]
    F --> G([End])
```

---

## 2. Preorder Traversal

```mermaid
flowchart TD
    A([Start]) --> B{Is Root NULL?}
    B -- Yes --> F([End])
    B -- No --> C[Visit Root]
    C --> D[Traverse Left Subtree]
    D --> E[Traverse Right Subtree]
    E --> F
```

**Order: Root → Left → Right**

---

## 3. Inorder Traversal

```mermaid
flowchart TD
    A([Start]) --> B{Is Root NULL?}
    B -- Yes --> F([End])
    B -- No --> C[Traverse Left Subtree]
    C --> D[Visit Root]
    D --> E[Traverse Right Subtree]
    E --> F
```

**Order: Left → Root → Right**

---

## 4. Postorder Traversal

```mermaid
flowchart TD
    A([Start]) --> B{Is Root NULL?}
    B -- Yes --> F([End])
    B -- No --> C[Traverse Left Subtree]
    C --> D[Traverse Right Subtree]
    D --> E[Visit Root]
    E --> F
```

**Order: Left → Right → Root**

---

## 5. Recursive Tree Traversal

```mermaid
flowchart TD
    A([Start]) --> B[Create Binary Tree]
    B --> C[Call Recursive Traversal Function]
    C --> D{Node Exists?}
    D -- No --> E[Return]
    D -- Yes --> F[Process Node According to Traversal Type]
    F --> G[Call Traversal for Child Nodes]
    G --> D
    E --> H([End])
```

---

## 6. Iterative Tree Traversal

```mermaid
flowchart TD
    A([Start]) --> B[Create Stack]
    B --> C[Push Root Node]
    C --> D{Stack Empty?}
    D -- No --> E[Pop Node]
    E --> F[Process Node]
    F --> G[Push Required Child Nodes]
    G --> D
    D -- Yes --> H([End])
```

---

## 7. Graph Using Adjacency Matrix

```mermaid
flowchart TD
    A([Start]) --> B[Set Number of Vertices]
    B --> C[Create Matrix with All Values 0]
    C --> D[Add Edges to Graph]
    D --> E[Update Matrix Values]
    E --> F[Display Adjacency Matrix]
    F --> G([End])
```

---

# Conclusion

These flowcharts represent the tree creation, traversal, and graph representation algorithms implemented in Unit 05.