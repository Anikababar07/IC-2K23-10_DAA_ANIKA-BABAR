# Traveling Salesperson Problem using Dynamic Programming

from functools import lru_cache


def traveling_salesperson(distance):
    n = len(distance)

    @lru_cache(maxsize=None)
    def tsp(current_city, visited_mask):
        # If all cities have been visited, return to the starting city
        if visited_mask == (1 << n) - 1:
            return distance[current_city][0]

        minimum_cost = float("inf")

        # Visit every unvisited city
        for next_city in range(n):
            if not (visited_mask & (1 << next_city)):
                cost = (
                    distance[current_city][next_city]
                    + tsp(
                        next_city,
                        visited_mask | (1 << next_city)
                    )
                )
                minimum_cost = min(minimum_cost, cost)

        return minimum_cost

    return tsp(0, 1)


def main():
    distance = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    minimum_cost = traveling_salesperson(distance)

    print("Traveling Salesperson Problem using Dynamic Programming")
    print("Minimum Cost:", minimum_cost)


if __name__ == "__main__":
    main()