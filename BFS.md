function BFS(graph, start):
    queue = [start]
    visited = set()
    while queue is not empty:
        node = dequeue(queue)
        if node not in visited:
            visit(node)
            add node to visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    enqueue(neighbor, queue)