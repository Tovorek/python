
class Graph:
    def __init__(self, r, t):
        self.adjList = [[] for _ in range(t)]
        for (src, dest) in r:
            self.adjList[src].append(dest)
 
def DFS(g, nod, explored):
    explored[nod] = True
    for u in g.adjList[nod]:
        if not explored[u]:
            DFS(g, u, explored)

def chck_strng_Conn(grph, vrtx):
    for i in range(n):
        visited = [False] * n
        DFS(graph, i, visited)
        for b in visited:
            if not b:
                return False
 
    return True
 
 
if __name__ == '__main__':
    edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
    n = 5
    graph = Graph(edges, n)
    if chck_strng_Conn(graph, n):
        print('The graph is strongly connected')
    else:
        print('The graph is not strongly connected')