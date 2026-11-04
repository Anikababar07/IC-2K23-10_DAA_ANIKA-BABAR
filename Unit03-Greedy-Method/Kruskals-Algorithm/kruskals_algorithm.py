class DisjointSet:
    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


def kruskals_algorithm(vertices, edges):
    # Sort all edges by increasing weight
    edges.sort(key=lambda edge: edge[2])

    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree = []
    total_cost = 0

    for source, destination, weight in edges:
        # Add edge only if it does not create a cycle
        if disjoint_set.union(source, destination):
            minimum_spanning_tree.append(
                (source, destination, weight)
            )
            total_cost += weight

            # MST contains exactly V - 1 edges
            if len(minimum_spanning_tree) == vertices - 1:
                break

    # Check whether a complete MST was formed
    if len(minimum_spanning_tree) != vertices - 1:
        return None, None

    return minimum_spanning_tree, total_cost


def main():
    try:
        vertices = int(input("Enter number of vertices: "))

        if vertices <= 0:
            print("Number of vertices must be positive.")
            return

        edge_count = int(input("Enter number of edges: "))

        if edge_count <= 0:
            print("Number of edges must be positive.")
            return

        edges = []

        print("\nEnter each edge as: source destination weight")
        print(f"Use vertex numbers from 0 to {vertices - 1}")

        for _ in range(edge_count):
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

            edges.append((source, destination, weight))

        mst, total_cost = kruskals_algorithm(vertices, edges)

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