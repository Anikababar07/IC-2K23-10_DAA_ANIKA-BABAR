# 0/1 Knapsack Using Dynamic Programming

## 1. Aim

To implement the 0/1 Knapsack problem using Dynamic Programming and find the maximum profit without exceeding the given capacity.

## 2. Problem Statement

Given a set of items, each with a weight and profit, select items such that the total weight does not exceed the knapsack capacity and the total profit is maximized. Each item can either be selected completely or not selected at all.

## 3. Algorithm / Approach

1. Create a Dynamic Programming table with rows representing items and columns representing capacities.
2. Initialize the first row and column with zero.
3. For each item and capacity, check whether the item can fit.
4. If it fits, choose the maximum between including and excluding the item.
5. If it does not fit, copy the value from the previous row.
6. The final cell contains the maximum possible profit.

## 4. Pseudocode

```text
FUNCTION Knapsack(weights, profits, capacity)

    n = number of items

    Create DP table of size (n + 1) × (capacity + 1)
    Initialize all values to 0

    FOR i = 1 TO n

        FOR currentCapacity = 0 TO capacity

            IF weights[i - 1] <= currentCapacity THEN

                includeItem =
                    profits[i - 1] +
                    dp[i - 1][currentCapacity - weights[i - 1]]

                excludeItem = dp[i - 1][currentCapacity]

                dp[i][currentCapacity] =
                    MAX(includeItem, excludeItem)

            ELSE

                dp[i][currentCapacity] =
                    dp[i - 1][currentCapacity]

            END IF

        END FOR

    END FOR

    RETURN dp[n][capacity]

END FUNCTION
```

## 5. Time Complexity

**O(n × W)**

Where:

- `n` = number of items
- `W` = knapsack capacity

## 6. Space Complexity

**O(n × W)** for the Dynamic Programming table.

## 7. Sample Input

```text
Number of items: 4

Item 1: Weight = 2, Profit = 3
Item 2: Weight = 3, Profit = 4
Item 3: Weight = 4, Profit = 5
Item 4: Weight = 5, Profit = 6

Knapsack Capacity: 5
```

## 8. Sample Output

```text
Maximum Profit: 7
```

## 9. Learning Outcomes

- Understood the concept of Dynamic Programming.
- Implemented the 0/1 Knapsack problem using a DP table.
- Learned the difference between including and excluding an item.
- Optimized the solution by storing solutions to smaller subproblems.