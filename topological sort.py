from collections import deque

class Graph:
    indegree = None
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        self.indegree = [0] * n
         for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.indegree[dest] = self.indegree[dest] + 1
def doTopologicalSort(graph, n):
    L = []
    indegree = graph.indegree
    S = deque([i for i in range(n) if indegree[i] == 0])
    while S:
        n = S.pop()
        L.append(n)
 
        for m in graph.adjList[n]:
            indegree[m] = indegree[m] - 1
            if indegree[m] == 0:
                S.append(m)
    for i in range(n):
        if indegree[i]:
            return None
 
    return L
 
 
if __name__ == '__main__':
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
    n = 8
    graph = Graph(edges, n)
    L = doTopologicalSort(graph, n)
    if L:
        print(L)    
    else:
        print('Graph has at least one cycle. Topological sorting is not possible.')