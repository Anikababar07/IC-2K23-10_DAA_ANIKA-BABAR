# Unit 05 - Basic Traversal and Search: Complexity Analysis

## 1. Binary Tree Creation

| Operation | Time Complexity |
|---|---|
| Creating nodes | O(n) |

**Space Complexity:** O(n), where n is the number of nodes.

---

## 2. Preorder Traversal

Each node is visited exactly once.

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

Where:
- `n` = number of nodes
- `h` = height of the tree

---

## 3. Inorder Traversal

Each node is visited exactly once.

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## 4. Postorder Traversal

Each node is visited exactly once.

- **Time Complexity:** O(n)
- **Space Complexity:** O(h)

---

## 5. Recursive Tree Traversal

All three recursive traversals visit every node once.

- **Time Complexity:** O(n)
- **Space Complexity:** O(h) due to the recursive call stack.

---

## 6. Iterative Tree Traversal

Each node is processed once using stacks.

| Traversal | Time Complexity | Space Complexity |
|---|---|---|
| Iterative Preorder | O(n) | O(h) |
| Iterative Inorder | O(n) | O(h) |
| Iterative Postorder | O(n) | O(n) |

---

## 7. Graph Using Adjacency Matrix

| Operation | Complexity |
|---|---|
| Creating adjacency matrix | O(V²) |
| Adding an edge | O(1) |
| Space Complexity | O(V²) |

Where `V` is the number of vertices.

---

# Complexity Comparison

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Binary Tree Creation | O(n) | O(n) |
| Preorder Traversal | O(n) | O(h) |
| Inorder Traversal | O(n) | O(h) |
| Postorder Traversal | O(n) | O(h) |
| Recursive Tree Traversal | O(n) | O(h) |
| Iterative Tree Traversal | O(n) | O(n) |
| Graph Adjacency Matrix | O(V²) | O(V²) |

---

# Conclusion

The tree traversal algorithms process each node once, resulting in linear time complexity. The adjacency matrix provides constant-time edge access but requires quadratic space based on the number of vertices.