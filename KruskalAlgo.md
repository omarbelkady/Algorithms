function Kruskal(graph):
    edges = sort all edges by weight
    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}
    MST = []
    for edge in edges:
        u, v, weight = edge
        if Find(parent, u) != Find(parent, v):
            Union(parent, rank, u, v)
            add edge to MST
    return MST