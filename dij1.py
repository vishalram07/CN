import heapq

def dijkstra(graph, start, end):
    """
    Compute the shortest path between start and end in the given graph using Dijkstra's algorithm.
    Returns the shortest path and its cost.
    """
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path, cost
            for neighbor, neighbor_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + neighbor_cost, neighbor, path))
    return None, None

# Define the network topology and link costs
network_topology = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 4},
    'C': {'A': 3, 'B': 2, 'D': 7},
    'D': {'B': 4, 'C': 7},
}

# Define the path for each IP fragment
fragment_paths = []
fragment_paths.append(['A', 'B', 'D'])  # path for fragment 1
fragment_paths.append(['A', 'C', 'D'])  # path for fragment 2
fragment_paths.append(['B', 'C', 'D'])  # path for fragment 3

# Compute the shortest path and its cost for each IP fragment
for i, path in enumerate(fragment_paths):
    start = path[0]
    end = path[-1]
    shortest_path, cost = dijkstra(network_topology, start, end)
    print("Shortest path for fragment {}: {}".format(i+1, shortest_path))
    print("Cost of shortest path for fragment {}: {}".format(i+1, cost))