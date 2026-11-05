# Multistage Graph using Dynamic Programming

INF = float('inf')


def shortest_path(graph):
    n = len(graph)

    # cost[i] stores the minimum cost from vertex i to destination
    cost = [INF] * n
    path = [-1] * n

    # Cost of destination vertex is 0
    cost[n - 1] = 0

    # Calculate minimum cost from right to left
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if graph[i][j] != INF:
                if graph[i][j] + cost[j] < cost[i]:
                    cost[i] = graph[i][j] + cost[j]
                    path[i] = j

    # Construct the shortest path
    shortest_path_vertices = []
    current = 0

    while current != -1:
        shortest_path_vertices.append(current)
        if current == n - 1:
            break
        current = path[current]

    return cost[0], shortest_path_vertices


def main():
    # Example multistage graph represented using an adjacency matrix
    graph = [
        [INF, 2, 1, 3, INF, INF, INF, INF],
        [INF, INF, INF, INF, 2, 3, INF, INF],
        [INF, INF, INF, INF, 6, 7, INF, INF],
        [INF, INF, INF, INF, INF, 6, 8, INF],
        [INF, INF, INF, INF, INF, INF, INF, 6],
        [INF, INF, INF, INF, INF, INF, INF, 4],
        [INF, INF, INF, INF, INF, INF, INF, 5],
        [INF, INF, INF, INF, INF, INF, INF, INF]
    ]

    minimum_cost, path = shortest_path(graph)

    print("Minimum Cost:", minimum_cost)
    print("Shortest Path:", " -> ".join(map(str, path)))


if __name__ == "__main__":
    main()