# Multistage Graph Using Dynamic Programming

## 1. Aim

To find the minimum cost path from a source vertex to a destination vertex in a multistage graph using Dynamic Programming.

## 2. Problem Statement

A multistage graph is a directed acyclic graph in which vertices are divided into different stages. The objective is to find the minimum-cost path from the source vertex to the destination vertex.

## 3. Algorithm / Approach

1. Represent the graph using an adjacency matrix.
2. Initialize the cost of the destination vertex as `0`.
3. Set the cost of all other vertices to infinity.
4. Process vertices from the destination towards the source.
5. For every vertex, find the minimum cost among all its possible next vertices.
6. Store the next vertex to reconstruct the shortest path.
7. Display the minimum cost and shortest path.

## 4. Pseudocode

```text
FUNCTION ShortestPath(graph)

    n = number of vertices

    Create cost array and initialize all values to INFINITY
    Create path array

    cost[destination] = 0

    FOR i = n - 2 DOWNTO 0

        FOR j = i + 1 TO n - 1

            IF edge exists from i to j THEN

                IF graph[i][j] + cost[j] < cost[i] THEN
                    cost[i] = graph[i][j] + cost[j]
                    path[i] = j
                END IF

            END IF

        END FOR

    END FOR

    RETURN cost[source] and path

END FUNCTION
```

## 5. Time Complexity

**O(V²)** when using an adjacency matrix, where `V` is the number of vertices.

## 6. Space Complexity

**O(V²)** due to the adjacency matrix.

## 7. Sample Output

```text
Minimum Cost: 8
Shortest Path: 0 -> 1 -> 5 -> 7
```

## 8. Learning Outcomes

- Understood the structure of a multistage graph.
- Applied Dynamic Programming to find an optimal path.
- Learned how to calculate minimum cost from destination to source.
- Implemented path reconstruction.