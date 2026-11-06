# Single-Source Shortest Path using Dijkstra's Algorithm

import heapq


def dijkstra(graph, source):
    distances = {vertex: float("inf") for vertex in graph}
    distances[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Update shortest distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 3)],
        "F": [("D", 6), ("E", 3)]
    }

    source = "A"
    distances = dijkstra(graph, source)

    print(f"Shortest distances from source vertex {source}:\n")

    for vertex, distance in distances.items():
        print(f"{source} -> {vertex} = {distance}")


if __name__ == "__main__":
    main()