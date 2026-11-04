# Unit 3 - Greedy Method: Complexity Analysis

This document presents the time and space complexity analysis of all algorithms implemented in Unit 3.

---

## 1. Fractional Knapsack

The Fractional Knapsack algorithm sorts items according to their profit-to-weight ratio and then selects items greedily.

| Operation | Complexity |
|---|---|
| Sorting items | O(n log n) |
| Selecting items | O(n) |
| Overall Time Complexity | O(n log n) |

**Space Complexity:** O(n) for storing items and selected item details.

---

## 2. Job Sequencing with Deadlines

The algorithm first sorts jobs by decreasing profit and then searches for an available slot before each job's deadline.

| Operation | Complexity |
|---|---|
| Sorting jobs | O(n log n) |
| Finding available slots | O(n × d) |
| Overall Time Complexity | O(n log n + n × d) |

Where `d` is the maximum deadline.

**Space Complexity:** O(d) for storing the time slots.

---

## 3. Prim's Algorithm

Prim's Algorithm uses a priority queue to repeatedly select the minimum-weight edge that connects an unvisited vertex.

| Operation | Complexity |
|---|---|
| Priority Queue Operations | O(log V) |
| Overall Time Complexity | O(E log V) |

Where:

- `V` = number of vertices
- `E` = number of edges

**Space Complexity:** O(V + E) for the graph, visited array, priority queue, and Minimum Spanning Tree.

---

## 4. Kruskal's Algorithm

Kruskal's Algorithm sorts all edges and uses the Disjoint Set (Union-Find) data structure to avoid cycles.

| Operation | Complexity |
|---|---|
| Sorting edges | O(E log E) |
| Union-Find operations | O(E × α(V)) |
| Overall Time Complexity | O(E log E) |

Where:

- `V` = number of vertices
- `E` = number of edges
- `α(V)` is the inverse Ackermann function and is nearly constant in practice.

**Space Complexity:** O(V + E) for storing the edges, Disjoint Set, and Minimum Spanning Tree.

---

# Complexity Comparison

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Fractional Knapsack | O(n log n) | O(n) |
| Job Sequencing | O(n log n + n × d) | O(d) |
| Prim's Algorithm | O(E log V) | O(V + E) |
| Kruskal's Algorithm | O(E log E) | O(V + E) |

---

# Conclusion

The complexity analysis shows that Greedy algorithms provide efficient solutions by making locally optimal choices. Fractional Knapsack and Job Sequencing rely on sorting, while Prim's and Kruskal's Algorithms efficiently solve Minimum Spanning Tree problems using priority queues and edge sorting.