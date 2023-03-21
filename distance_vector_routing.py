def dvr(graph,start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    routing_table = {node: {'distance': distances[node], 'next_hop': None} for node in graph}
    while True:
        updates = False
        for node in graph:
            for neighbor, weight in graph[node].items():
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    routing_table[neighbor]['distance'] = new_distance
                    routing_table[neighbor]['next_hop'] = node
                    updates = True
        if not updates:
            break
    return routing_table
graph={'A':{'B':2,'D':1,'C':5},
       'B':{'A':2,'D':2,'C':3},
       'C':{'B':3,'D':3,'E':1,'F':5},
       'D':{'A':1,'B':2,'E':1,'C':3},
       'E':{'D':1,'F':2,'C':1},
       'F':{'C':5,'E':2}
       }
routing_tables = {}
for node in graph:
    routing_tables[node] = dvr(graph, node)
print("INITIAL ROUTING TABLES\n")
for node in graph:
    print("ROUTING TABLE FOR NODE", node)
    print(routing_tables[node])
    print()
vectors = {'D': {'E': {'distance': 1, 'next_hop': 'D'}},
           'B': {'A': {'distance': 2, 'next_hop': 'B'}},
           'E': {'F': {'distance': 2, 'next_hop': 'E'}}}
while True:
    updates = False
    for node in graph:
        for neighbor in graph[node]:
            if neighbor in vectors.get(node, {}):
                distance = vectors[node][neighbor]['distance']
                next_hop = neighbor
                if distance < routing_tables[node][neighbor]['distance']:
                    routing_tables[node][neighbor]['distance'] = distance
                    routing_tables[node][neighbor]['next_hop'] = next_hop
                    updates = True
        if not updates:
            break
    if not updates:
        break
print("FINAL ROUTING TABLES\n")
for node in graph:
    print("ROUTING TABLE FOR NODE", node)
    print(routing_tables[node])
    print()  
    print("ROUTING TABLE AT NODE", node)
    print("Destination\tDistance\tNext Hop")
    for destination, data in routing_tables[node].items():
        print(destination, "\t\t", data['distance'], "\t\t", data['next_hop'])
    print()
