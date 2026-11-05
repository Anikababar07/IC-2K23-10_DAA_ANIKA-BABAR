# Single-Source Shortest Path Using Dijkstra's Algorithm

## 1. Aim

To find the shortest distance from a single source vertex to all other vertices in a weighted graph using Dijkstra's Algorithm.

## 2. Problem Statement

Given a weighted graph and a source vertex, determine the minimum distance from the source to every other vertex.

## 3. Algorithm / Approach

1. Set the distance of the source vertex to `0`.
2. Set the distance of all other vertices to infinity.
3. Insert the source vertex into a priority queue.
4. Select the vertex with the minimum distance.
5. Update the distances of its neighboring vertices.
6. Repeat until all reachable vertices are processed.
7. Display the shortest distances from the source.

## 4. Pseudocode

```text
FUNCTION Dijkstra(graph, source)

    Set distance of every vertex to INFINITY
    distance[source] = 0

    Create priority queue
    Add source with distance 0

    WHILE priority queue is not empty

        currentVertex = vertex with minimum distance

        FOR each neighbor of currentVertex

            newDistance =
                distance[currentVertex] + edgeWeight

            IF newDistance < distance[neighbor] THEN
                distance[neighbor] = newDistance
                Add neighbor to priority queue
            END IF

        END FOR

    END WHILE

    RETURN distances

END FUNCTION
```

## 5. Time Complexity

Using a priority queue:

**O((V + E) log V)**

Where `V` is the number of vertices and `E` is the number of edges.

## 6. Space Complexity

**O(V + E)** for storing the graph, distances, and priority queue.

## 7. Sample Output

```text
Shortest distances from source vertex A:

A -> A = 0
A -> B = 3
A -> C = 2
A -> D = 8
A -> E = 10
A -> F = 13
```

## 8. Learning Outcomes

- Understood the Single-Source Shortest Path problem.
- Implemented Dijkstra's Algorithm using a priority queue.
- Learned how shortest distances are updated using relaxation.
- Analyzed the efficiency of Dijkstra's Algorithm.