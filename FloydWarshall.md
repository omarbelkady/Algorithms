function FloydWarshall(graph):
    distances = graph
    for k from 0 to |V|-1:
        for i from 0 to |V|-1:
            for j from 0 to |V|-1:
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances