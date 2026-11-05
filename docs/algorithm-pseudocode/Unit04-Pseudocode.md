# Unit 4 - Dynamic Programming: Algorithm Pseudocode

## 1. Fibonacci Using Recursion

```text
FUNCTION Fibonacci(n)

    IF n <= 1 THEN
        RETURN n
    END IF

    RETURN Fibonacci(n - 1) + Fibonacci(n - 2)

END FUNCTION
```

---

## 2. Fibonacci Using Memoization

```text
FUNCTION Fibonacci(n, memo)

    IF n <= 1 THEN
        RETURN n
    END IF

    IF memo[n] is already calculated THEN
        RETURN memo[n]
    END IF

    memo[n] = Fibonacci(n - 1, memo) + Fibonacci(n - 2, memo)

    RETURN memo[n]

END FUNCTION
```

---

## 3. 0/1 Knapsack

```text
FUNCTION Knapsack(weights, profits, capacity)

    n = number of items

    Create DP table of size (n + 1) × (capacity + 1)
    Initialize all values to 0

    FOR i = 1 TO n

        FOR w = 0 TO capacity

            IF weights[i - 1] <= w THEN

                includeItem =
                    profits[i - 1] +
                    dp[i - 1][w - weights[i - 1]]

                excludeItem = dp[i - 1][w]

                dp[i][w] = MAX(includeItem, excludeItem)

            ELSE
                dp[i][w] = dp[i - 1][w]
            END IF

        END FOR

    END FOR

    RETURN dp[n][capacity]

END FUNCTION
```

---

## 4. Multistage Graph

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

---

## 5. Floyd-Warshall Algorithm

```text
FUNCTION FloydWarshall(graph)

    distance = copy of graph
    vertices = number of vertices

    FOR k = 0 TO vertices - 1

        FOR i = 0 TO vertices - 1

            FOR j = 0 TO vertices - 1

                IF distance[i][k] + distance[k][j] < distance[i][j] THEN

                    distance[i][j] =
                        distance[i][k] + distance[k][j]

                END IF

            END FOR

        END FOR

    END FOR

    RETURN distance

END FUNCTION
```

---

## 6. Single-Source Shortest Path (Dijkstra's Algorithm)

```text
FUNCTION Dijkstra(graph, source)

    Set distance of every vertex to INFINITY
    distance[source] = 0

    Create priority queue
    Add source with distance 0

    WHILE priority queue is not empty

        currentVertex = vertex with minimum distance

        IF current distance is outdated THEN
            CONTINUE
        END IF

        FOR each neighbor of currentVertex

            newDistance =
                distance[currentVertex] + edgeWeight

            IF newDistance < distance[neighbor] THEN
                distance[neighbor] = newDistance
                Add neighbor to priority queue
            END IF

        END FOR

    END WHILE

    RETURN distance

END FUNCTION
```

---

## 7. Traveling Salesperson Problem

```text
FUNCTION TSP(currentCity, visitedMask)

    IF all cities are visited THEN
        RETURN distance[currentCity][startingCity]
    END IF

    minimumCost = INFINITY

    FOR each city

        IF city is not visited THEN

            cost = distance[currentCity][city]
                   + TSP(city, updatedVisitedMask)

            minimumCost = MIN(minimumCost, cost)

        END IF

    END FOR

    RETURN minimumCost

END FUNCTION
```

---

# Conclusion

This document contains language-independent pseudocode for all algorithms implemented in Unit 4 using Dynamic Programming.