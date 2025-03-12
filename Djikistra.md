function Dijkstra(graph, start):
    distances = {node: infinity for node in graph}
    distances[start] = 0
    priorityQueue = [(0, start)]
    while priorityQueue is not empty:
        currentDistance, currentNode = extractMin(priorityQueue)
        if currentDistance > distances[currentNode]:
            continue
        for neighbor, weight in graph[currentNode]:
            distance = currentDistance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                insert(distance, neighbor, priorityQueue)
    return distances