def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = set(graph)
    while unvisited:
        current_node = min(unvisited, key=distances.get)
        unvisited.remove(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    return distances
graph = {'A': {'B': 3, 'D': 7},
         'B': {'A': 3, 'C':4,'D': 2},
         'C': {'B': 4, 'D': 5, 'E': 6},
         'D': {'A': 7, 'B':2,'C': 5, 'E': 4},
         'E': {'C': 6, 'D': 4}}
for i in graph:
    distances = dijkstra(graph, i)
    print(distances)  
    