import heapq


def prims_algorithm(graph, vertices):
    visited = [False] * vertices
    minimum_spanning_tree = []
    total_cost = 0

    # Start from vertex 0
    priority_queue = [(0, 0, -1)]

    while priority_queue:
        weight, current, parent = heapq.heappop(priority_queue)

        if visited[current]:
            continue

        visited[current] = True
        total_cost += weight

        # Add edge to MST (except for starting vertex)
        if parent != -1:
            minimum_spanning_tree.append(
                (parent, current, weight)
            )

        # Add all unvisited neighboring vertices
        for neighbor, edge_weight in graph[current]:
            if not visited[neighbor]:
                heapq.heappush(
                    priority_queue,
                    (edge_weight, neighbor, current)
                )

    # Check whether all vertices are connected
    if not all(visited):
        return None, None

    return minimum_spanning_tree, total_cost


def main():
    try:
        vertices = int(input("Enter number of vertices: "))

        if vertices <= 0:
            print("Number of vertices must be positive.")
            return

        edges = int(input("Enter number of edges: "))

        if edges <= 0:
            print("Number of edges must be positive.")
            return

        graph = [[] for _ in range(vertices)]

        print("\nEnter each edge as: source destination weight")
        print(
            f"Use vertex numbers from 0 to {vertices - 1}"
        )

        for _ in range(edges):
            source, destination, weight = map(
                int,
                input().split()
            )

            if (
                source < 0
                or source >= vertices
                or destination < 0
                or destination >= vertices
            ):
                print("Invalid vertex number.")
                return

            graph[source].append((destination, weight))
            graph[destination].append((source, weight))

        mst, total_cost = prims_algorithm(graph, vertices)

        if mst is None:
            print(
                "\nThe graph is disconnected. "
                "A Minimum Spanning Tree cannot be formed."
            )
            return

        print("\nEdges in the Minimum Spanning Tree:")

        for source, destination, weight in mst:
            print(
                f"{source} -- {destination} "
                f"(Weight: {weight})"
            )

        print(f"\nTotal Cost of MST: {total_cost}")

    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()