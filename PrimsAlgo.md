function Prim(graph):
    MST = []
    visited = set()
    priorityQueue = [(0, start)]
    while priorityQueue is not empty:
        weight, node = extractMin(priorityQueue)
        if node not in visited:
            add edge to MST
            add node to visited
            for neighbor, edgeWeight in graph[node]:
                if neighbor not in visited:
                    insert(edgeWeight, neighbor, priorityQueue)
    return MST