def dijkstra(graph, start):
    shortest = {}
    unvisited = graph.copy()
    inf = float('inf')
    path = {}

    # Initialize all distances to infinity
    for node in unvisited:
        shortest[node] = inf
    shortest[start] = 0  # Distance to the start node is 0

    while unvisited:
        min_node = None
        for node in unvisited:
            if min_node is None or shortest[node] < shortest[min_node]:
                min_node = node

        for neighbor, weight in graph[min_node].items():
            if weight + shortest[min_node] < shortest[neighbor]:
                shortest[neighbor] = weight + shortest[min_node]
                path[neighbor] = min_node

        unvisited.pop(min_node)  # Mark node as visited

    return shortest, path

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances, paths = dijkstra(graph, 'A')
print("Shortest distances:", distances)
print("Paths:", paths)
