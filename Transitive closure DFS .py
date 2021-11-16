
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
def DFS(graph, C, root, descendant):
    for child in graph.adjList[descendant]:
        if C[root][child] == 0:
            C[root][child] = 1
            DFS(graph, C, root, child)
 
 
if __name__ == '__main__':
 
    edges = [(0, 2), (1, 0), (3, 1)]
    n = 4
    graph = Graph(edges, n)
    C = [[0 for x in range(n)] for y in range(n)]
    for v in range(n):
        C[v][v] = 1
        DFS(graph, C, v, v)
        print(C[v])
 
