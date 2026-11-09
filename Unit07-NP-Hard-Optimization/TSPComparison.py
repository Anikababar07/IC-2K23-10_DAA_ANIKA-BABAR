# Compare Travelling Salesperson Problem (TSP)
# using Dynamic Programming and Branch and Bound

import time
from functools import lru_cache


# Dynamic Programming Approach
def tsp_dynamic_programming(graph):
    n = len(graph)
    ALL_VISITED = (1 << n) - 1

    @lru_cache(None)
    def solve(mask, current_city):
        # If all cities are visited, return to the starting city
        if mask == ALL_VISITED:
            return graph[current_city][0]

        minimum_cost = float("inf")

        # Visit each unvisited city
        for next_city in range(n):
            if not (mask & (1 << next_city)):
                cost = (
                    graph[current_city][next_city]
                    + solve(mask | (1 << next_city), next_city)
                )
                minimum_cost = min(minimum_cost, cost)

        return minimum_cost

    return solve(1, 0)


# Branch and Bound Approach
def tsp_branch_and_bound(graph):
    n = len(graph)
    minimum_cost = float("inf")

    def solve(current_city, visited, current_cost, count):
        nonlocal minimum_cost

        # Prune paths that are already more expensive
        if current_cost >= minimum_cost:
            return

        # All cities have been visited
        if count == n:
            total_cost = current_cost + graph[current_city][0]
            minimum_cost = min(minimum_cost, total_cost)
            return

        # Try all unvisited cities
        for next_city in range(n):
            if not visited[next_city]:
                visited[next_city] = True

                solve(
                    next_city,
                    visited,
                    current_cost + graph[current_city][next_city],
                    count + 1
                )

                # Backtrack
                visited[next_city] = False

    visited = [False] * n
    visited[0] = True

    solve(0, visited, 0, 1)

    return minimum_cost


# Example distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


# Dynamic Programming execution
start = time.perf_counter()
dp_result = tsp_dynamic_programming(graph)
dp_time = time.perf_counter() - start


# Branch and Bound execution
start = time.perf_counter()
bb_result = tsp_branch_and_bound(graph)
bb_time = time.perf_counter() - start


# Display results
print("TSP Algorithm Comparison")
print("-" * 35)

print("\nDynamic Programming:")
print("Minimum Cost:", dp_result)
print("Execution Time:", dp_time, "seconds")

print("\nBranch and Bound:")
print("Minimum Cost:", bb_result)
print("Execution Time:", bb_time, "seconds")