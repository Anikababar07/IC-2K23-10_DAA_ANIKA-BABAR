# Unit 3 - Greedy Method: Algorithm Pseudocode

## 1. Fractional Knapsack

```text
FUNCTION FractionalKnapsack(items, capacity)

    Sort items in decreasing order of profit/weight ratio

    totalProfit = 0

    FOR each item

        IF capacity == 0 THEN
            BREAK
        END IF

        IF item.weight <= capacity THEN
            Add complete item
            capacity = capacity - item.weight
            totalProfit = totalProfit + item.profit

        ELSE
            fraction = capacity / item.weight
            totalProfit = totalProfit + item.profit × fraction
            capacity = 0

        END IF

    END FOR

    RETURN totalProfit

END FUNCTION
```

---

## 2. Job Sequencing with Deadlines

```text
FUNCTION JobSequencing(jobs)

    Sort jobs in decreasing order of profit

    maxDeadline = maximum deadline among all jobs

    Create empty slots from 1 to maxDeadline
    totalProfit = 0

    FOR each job in sorted jobs

        FOR slot = job.deadline DOWNTO 1

            IF slot is empty THEN
                Schedule job in slot
                totalProfit = totalProfit + job.profit
                BREAK
            END IF

        END FOR

    END FOR

    RETURN scheduled jobs and totalProfit

END FUNCTION
```

---

## 3. Prim's Algorithm

```text
FUNCTION Prims(graph, vertices)

    Mark all vertices as unvisited

    Select a starting vertex
    Add starting vertex to priority queue

    WHILE priority queue is not empty

        Remove minimum-weight edge

        IF current vertex is already visited THEN
            CONTINUE
        END IF

        Mark current vertex as visited

        IF current vertex has a parent THEN
            Add edge to MST
            Add edge weight to totalCost
        END IF

        FOR each neighbor of current vertex

            IF neighbor is not visited THEN
                Add neighbor edge to priority queue
            END IF

        END FOR

    END WHILE

    IF all vertices are visited THEN
        RETURN MST and totalCost
    ELSE
        RETURN "Graph is disconnected"
    END IF

END FUNCTION
```

---

## 4. Kruskal's Algorithm

```text
FUNCTION Kruskals(vertices, edges)

    Sort all edges in increasing order of weight

    Create Disjoint Set for all vertices

    MST = empty
    totalCost = 0

    FOR each edge (source, destination, weight)

        IF Find(source) is not equal to Find(destination) THEN

            Add edge to MST
            totalCost = totalCost + weight

            Union(source, destination)

        END IF

        IF number of edges in MST == vertices - 1 THEN
            BREAK
        END IF

    END FOR

    IF number of edges in MST == vertices - 1 THEN
        RETURN MST and totalCost
    ELSE
        RETURN "Graph is disconnected"
    END IF

END FUNCTION
```

---

# Conclusion

This document contains language-independent pseudocode for all algorithms implemented in Unit 3 using the Greedy Method.
