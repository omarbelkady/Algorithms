```plaintext
function DFS(graph, node, visited):
    if node not in visited:
        visit(node)
        add node to visited
        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)
```
