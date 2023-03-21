class Edge :
    def __init__(self, src, dst, weight) :
         self.src = src 
         self.dst = dst 
         self.weight = weight
class Graph :
    def __init__(self, edge_list, node_cnt) :
         self.edge_list = edge_list
         self.node_cnt  = node_cnt
    def BellmanFord (self, src) :
        distance = [999999999999] * self.node_cnt
        distance[src] = 0 
        for node in range(self.node_cnt-1) :
            for edge in self.edge_list :
                if (distance[edge.dst] > distance[edge.src] + edge.weight) :
                    distance[edge.dst] = distance[edge.src] + edge.weight
        for node in range(self.node_cnt) : 
            print("Source Node("+str(src)+") -> Destination Node("+str(node)+") : Length => "+str(distance[node]))
e01 = Edge(0, 1, 4) 
e05 = Edge(0, 2, 2)
e12 = Edge(1, 2, 3)
e15 = Edge(2, 1, 1) 
e23 = Edge(1, 3, 2)
e24 = Edge(2, 3, 4)
e43 = Edge(4, 3, -5) 
e45 = Edge(1, 4, 3)
e51 = Edge(2, 4, 5)
edge_list = [e01, e05, e12, e15, e23, e24, e43, e45, e51]
node_cnt = 5
source_node = 0
g = Graph(edge_list, node_cnt)
g.BellmanFord(source_node)



