# Travelling Salesperson Problem using Branch and Bound

import math


def calculate_bound(graph, visited, current_city, current_cost):
    """Calculate a simple lower bound for the remaining path."""
    bound = current_cost
    n = len(graph)

    # Add minimum outgoing edge for each unvisited city
    for city in range(n):
        if not visited[city]:
            minimum = math.inf
            for next_city in range(n):
                if city != next_city and graph[city][next_city] < minimum:
                    minimum = graph[city][next_city]

            if minimum != math.inf:
                bound += minimum

    return bound


def tsp_branch_bound(graph):
    n = len(graph)
    min_cost = math.inf
    best_path = []

    def solve(current_city, visited, path, current_cost):
        nonlocal min_cost, best_path

        # All cities are visited
        if len(path) == n:
            total_cost = current_cost + graph[current_city][0]

            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [0]

            return

        # Calculate lower bound
        lower_bound = calculate_bound(
            graph, visited, current_city, current_cost
        )

        # Prune this path if it cannot give a better solution
        if lower_bound >= min_cost:
            return

        # Try all unvisited cities
        for next_city in range(n):
            if not visited[next_city] and graph[current_city][next_city] > 0:
                visited[next_city] = True

                solve(
                    next_city,
                    visited,
                    path + [next_city],
                    current_cost + graph[current_city][next_city]
                )

                # Backtrack
                visited[next_city] = False

    visited = [False] * n
    visited[0] = True

    solve(0, visited, [0], 0)

    return min_cost, best_path


# Example distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp_branch_bound(graph)

print("Minimum Cost:", cost)
print("Optimal Path:", " -> ".join(map(str, path)))