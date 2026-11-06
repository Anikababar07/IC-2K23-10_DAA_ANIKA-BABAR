# All-Pairs Shortest Path Using Floyd-Warshall Algorithm

## 1. Aim

To find the shortest paths between all pairs of vertices in a weighted graph using the Floyd-Warshall algorithm.

## 2. Problem Statement

Given a weighted graph, find the minimum distance between every pair of vertices. The Floyd-Warshall algorithm uses Dynamic Programming to improve the shortest paths by considering each vertex as an intermediate vertex.

## 3. Algorithm / Approach

1. Represent the graph using an adjacency matrix.
2. Initialize the distance matrix with the graph's edge weights.
3. For every vertex `k`, consider it as an intermediate vertex.
4. For every pair of vertices `(i, j)`, check whether the path through `k` is shorter.
5. Update the distance if a shorter path is found.
6. Display the final shortest-distance matrix.

## 4. Pseudocode

```text
FUNCTION FloydWarshall(graph)

    distance = copy of graph
    vertices = number of vertices

    FOR k = 0 TO vertices - 1
        FOR i = 0 TO vertices - 1
            FOR j = 0 TO vertices - 1

                IF distance[i][k] + distance[k][j] < distance[i][j]
                    distance[i][j] =
                        distance[i][k] + distance[k][j]
                END IF

            END FOR
        END FOR
    END FOR

    RETURN distance

END FUNCTION
```

## 5. Time Complexity

**O(V³)**, where `V` is the number of vertices.

## 6. Space Complexity

**O(V²)** for the distance matrix.

## 7. Sample Output

```text
Shortest Distance Matrix:
0       5       8       9
INF     0       3       4
INF     INF     0       1
INF     INF     INF     0
```

## 8. Learning Outcomes

- Understood the all-pairs shortest path problem.
- Implemented the Floyd-Warshall algorithm using Dynamic Programming.
- Learned how intermediate vertices improve shortest paths.
- Analyzed the time and space complexity of the algorithm.