# Graph Representation Using Adjacency Matrix

# Number of vertices
vertices = 5

# Create an adjacency matrix filled with 0
graph = [[0 for _ in range(vertices)] for _ in range(vertices)]


# Function to add an edge
def add_edge(source, destination):
    graph[source][destination] = 1
    graph[destination][source] = 1


# Add edges to the graph
add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 4)


# Display the adjacency matrix
print("Adjacency Matrix:")

for row in graph:
    print(row)