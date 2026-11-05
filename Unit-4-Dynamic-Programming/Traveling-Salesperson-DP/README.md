# Traveling Salesperson Problem Using Dynamic Programming

## 1. Aim

To solve the Traveling Salesperson Problem using Dynamic Programming and find the minimum-cost tour that visits every city exactly once and returns to the starting city.

## 2. Problem Statement

Given a set of cities and the distance between every pair of cities, find the minimum-cost route that starts from a city, visits every other city exactly once, and returns to the starting city.

## 3. Algorithm / Approach

1. Represent the distances between cities using a matrix.
2. Use a bitmask to represent the set of visited cities.
3. Define a Dynamic Programming state using the current city and visited cities.
4. If all cities are visited, return the cost of returning to the starting city.
5. For every unvisited city, calculate the cost of visiting that city.
6. Store previously calculated states using memoization.
7. Return the minimum possible tour cost.

## 4. Pseudocode

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

## 5. Time Complexity

**O(n² × 2ⁿ)**

The Dynamic Programming approach stores and reuses solutions for different combinations of visited cities.

## 6. Space Complexity

**O(n × 2ⁿ)** for storing the Dynamic Programming states.

## 7. Sample Output

```text
Traveling Salesperson Problem using Dynamic Programming
Minimum Cost: 80
```

## 8. Learning Outcomes

- Understood the Traveling Salesperson Problem.
- Applied Dynamic Programming with memoization.
- Used bitmasking to represent visited cities.
- Learned how Dynamic Programming reduces repeated calculations.