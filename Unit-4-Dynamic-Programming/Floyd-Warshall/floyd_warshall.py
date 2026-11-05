# All-Pairs Shortest Path using Floyd-Warshall Algorithm

INF = float("inf")


def floyd_warshall(graph):
    vertices = len(graph)

    # Create a copy of the graph for storing shortest distances
    distance = [row[:] for row in graph]

    # Try each vertex as an intermediate vertex
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


def print_solution(distance):
    print("\nShortest Distance Matrix:")

    for row in distance:
        for value in row:
            if value == INF:
                print("INF", end="\t")
            else:
                print(value, end="\t")
        print()


def main():
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    distance = floyd_warshall(graph)
    print_solution(distance)


if __name__ == "__main__":
    main()