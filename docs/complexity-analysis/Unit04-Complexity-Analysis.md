# Unit 4 - Dynamic Programming: Complexity Analysis

This document presents the time and space complexity analysis of all algorithms implemented in Unit 4.

---

## 1. Fibonacci Using Recursion

The recursive approach calculates the same Fibonacci values repeatedly.

| Operation | Complexity |
| --- | --- |
| Recursive calculations | O(2ⁿ) |
| Overall Time Complexity | O(2ⁿ) |

**Space Complexity:** O(n) due to the recursive call stack.

---

## 2. Fibonacci Using Memoization

Memoization stores previously calculated Fibonacci values and avoids repeated calculations.

| Operation | Complexity |
| --- | --- |
| Calculating each Fibonacci value once | O(n) |
| Overall Time Complexity | O(n) |

**Space Complexity:** O(n) for the memoization array and recursive call stack.

---

## 3. 0/1 Knapsack

The algorithm uses a Dynamic Programming table to store the maximum profit for different items and capacities.

| Operation | Complexity |
| --- | --- |
| Filling DP table | O(n × W) |
| Overall Time Complexity | O(n × W) |

Where:

- `n` = number of items
- `W` = knapsack capacity

**Space Complexity:** O(n × W) for the DP table.

---

## 4. Multistage Graph

The algorithm calculates the minimum cost by processing vertices from the destination towards the source.

| Operation | Complexity |
| --- | --- |
| Checking possible paths | O(V²) |
| Overall Time Complexity | O(V²) |

Where `V` is the number of vertices.

**Space Complexity:** O(V²) for the adjacency matrix representation.

---

## 5. Floyd-Warshall Algorithm

Floyd-Warshall checks every possible intermediate vertex for every pair of vertices.

| Operation | Complexity |
| --- | --- |
| Three nested loops | O(V³) |
| Overall Time Complexity | O(V³) |

Where `V` is the number of vertices.

**Space Complexity:** O(V²) for the distance matrix.

---

## 6. Single-Source Shortest Path (Dijkstra's Algorithm)

Dijkstra's Algorithm uses a priority queue to efficiently select the next minimum-distance vertex.

| Operation | Complexity |
| --- | --- |
| Priority queue operations | O(log V) |
| Overall Time Complexity | O((V + E) log V) |

Where:

- `V` = number of vertices
- `E` = number of edges

**Space Complexity:** O(V + E).

---

## 7. Traveling Salesperson Problem

The Dynamic Programming approach uses memoization and bitmasking to avoid solving the same subproblems repeatedly.

| Operation | Complexity |
| --- | --- |
| Dynamic Programming states | O(n² × 2ⁿ) |
| Overall Time Complexity | O(n² × 2ⁿ) |

Where `n` is the number of cities.

**Space Complexity:** O(n × 2ⁿ) for storing Dynamic Programming states.

---

# Complexity Comparison

| Algorithm | Time Complexity | Space Complexity |
| --- | --- | --- |
| Fibonacci Recursion | O(2ⁿ) | O(n) |
| Fibonacci Memoization | O(n) | O(n) |
| 0/1 Knapsack | O(n × W) | O(n × W) |
| Multistage Graph | O(V²) | O(V²) |
| Floyd-Warshall | O(V³) | O(V²) |
| Dijkstra's Algorithm | O((V + E) log V) | O(V + E) |
| Traveling Salesperson | O(n² × 2ⁿ) | O(n × 2ⁿ) |

---

# Conclusion

The complexity analysis shows how Dynamic Programming improves efficiency by storing and reusing solutions to overlapping subproblems. Memoization significantly improves Fibonacci performance, while Dynamic Programming provides efficient solutions for optimization and shortest-path problems.