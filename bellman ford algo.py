import sys
def getPath(parent, vertex):
    if vertex < 0:
        return []
    return getPath(parent, parent[vertex]) + [vertex]
def bellmanFord(edges, source, n):
    distance = [sys.maxsize] * n
    parent = [-1] * n
    distance[source] = 0
    for k in range(n - 1):
        for (u, v, w) in edges:
            if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
    for (u, v, w) in edges: 
        if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
            print('Negative-weight cycle is found!!')
            return
 
    for i in range(n):
        if i != source and distance[i] < sys.maxsize:
            print(f'The distance of vertex {i} from vertex {source} is {distance[i]}. '
                  f'Its path is', getPath(parent, i))
 
 
if __name__ == '__main__':
    edges = [
        (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
        (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
    ]
    n = 5
    for source in range(n):
        bellmanFord(edges, source, n)