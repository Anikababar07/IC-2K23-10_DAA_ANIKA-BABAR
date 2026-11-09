# Unit 07 - NP-Hard, NP-Complete & Advanced Optimization

## 1. Exhaustive Search

```text
START

INPUT a list of numbers
SET largest = first number

FOR each number in the list
    IF number is greater than largest
        SET largest = number
    END IF
END FOR

DISPLAY largest number

END
```

---

## 2. 0/1 Knapsack using Branch and Bound

```text
FUNCTION Knapsack(capacity, weights, profits)

    SORT items according to profit-to-weight ratio

    CREATE root node
    ADD root node to queue

    SET maximum profit = 0

    WHILE queue is not empty

        REMOVE a node from queue

        CREATE a node by including the next item

        IF included node is within capacity
            UPDATE maximum profit
        END IF

        CALCULATE bound of included node

        IF bound is greater than maximum profit
            ADD included node to queue
        END IF

        CREATE a node by excluding the next item

        CALCULATE bound of excluded node

        IF bound is greater than maximum profit
            ADD excluded node to queue
        END IF

    END WHILE

    RETURN maximum profit

END FUNCTION
```

---

## 3. TSP using Branch and Bound

```text
FUNCTION Solve(currentCity, visited, path, currentCost)

    IF all cities are visited
        ADD cost to return to starting city

        IF total cost is less than minimum cost
            UPDATE minimum cost
            SAVE best path
        END IF

        RETURN
    END IF

    CALCULATE lower bound

    IF lower bound is greater than or equal to minimum cost
        RETURN
    END IF

    FOR each unvisited city

        MARK city as visited

        CALL Solve for the next city

        MARK city as unvisited

    END FOR

END FUNCTION
```

---

## 4. 0/1 Knapsack: Dynamic Programming vs Branch and Bound

### Dynamic Programming

```text
CREATE a DP table

FOR each item
    FOR each possible capacity

        IF item weight is less than or equal to capacity
            CHOOSE maximum of:
                Include the item
                Exclude the item
        ELSE
            EXCLUDE the item
        END IF

    END FOR
END FOR

RETURN maximum profit
```

### Branch and Bound

```text
START with first item

FOR each item
    TRY including the item

    IF weight exceeds capacity
        STOP current branch
    END IF

    UPDATE maximum profit

    TRY excluding the item

END FOR

RETURN maximum profit
```

---

## 5. TSP: Dynamic Programming vs Branch and Bound

### Dynamic Programming

```text
FUNCTION Solve(mask, currentCity)

    IF all cities are visited
        RETURN cost to starting city
    END IF

    SET minimum cost to infinity

    FOR each unvisited city
        CALCULATE cost of visiting the city
        UPDATE minimum cost
    END FOR

    RETURN minimum cost

END FUNCTION
```

### Branch and Bound

```text
START from the first city

TRY every unvisited city

IF current path cost is greater than minimum cost
    PRUNE the path
END IF

IF all cities are visited
    ADD return cost to starting city
    UPDATE minimum cost
END IF

BACKTRACK and try another city

RETURN minimum cost
```

---

# Conclusion

This document contains the pseudocode for the NP-Hard and advanced optimization algorithms implemented in Unit 07.