import sys
A = [[0, 4, 3, 0, 7, 0, 0],
    [4, 0, 6, 5, 0, 0, 0],
    [3, 6, 0, 11, 8, 0, 0],
    [0, 5, 11, 0, 2, 2, 10],
    [7, 0, 8, 2, 0, 0, 5],
    [0, 0, 0, 2, 0, 0, 3],
    [0, 0, 0, 10, 5, 3, 0],
    ]



class Graph():
    def __init__(self,vertx):
        
        self.graph = [[0 for colum in range(vertx)] for row in range(vertx)]
        self.V = len(self.graph)

    def get_graph(self):
        return self.graph
    def get_V(self):
        return self.V

    def get_node_min_distance(self, dist, visit_nodes):
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and visit_nodes[v] == False:
                min = dist[v]
                min_index = v
        print(str("min")+str(min_index))
        return min_index

    
    def dijktra(self, source):
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        visit_nodes = [False] * self.V

        for i in range(self.V):

            nodo_menor_valor = self.get_node_min_distance(dist, visit_nodes)
            print(nodo_menor_valor)
            visit_nodes[nodo_menor_valor] = True
            for v in range(self.V):
                if self.graph[nodo_menor_valor][v] > 0 and visit_nodes[v] == False and dist[v] > dist[nodo_menor_valor] + self.graph[nodo_menor_valor][v]: 
                    dist[v] = dist[nodo_menor_valor] + self.graph[nodo_menor_valor][v]
           

        for node in range(self.V):
            print(node, "t", dist[node])

            


                

        
            


g = Graph(7)
g.graph = A

print(g.get_graph())
print(g.get_V())
g.dijktra(0)
