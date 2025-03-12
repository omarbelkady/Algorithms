function TopologicalSort(graph):
    inDegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            inDegree[neighbor] += 1
    queue = [node for node in graph if inDegree[node] == 0]
    result = []
    while queue is not empty:
        node = dequeue(queue)
        result.append(node)
        for neighbor in graph[node]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                enqueue(neighbor, queue)
    if length(result) != |V|:
        return "Cycle detected"
    return result