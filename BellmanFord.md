function BellmanFord(graph, start):
    distances = {node: infinity for node in graph}
    distances[start] = 0
    for i from 1 to |V|-1:
        for edge(u, v, w) in graph:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    for edge(u, v, w) in graph:
        if distances[u] + w < distances[v]:
            return "Negative cycle detected"
    return distances