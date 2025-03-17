```plaintext
function TarjanSCC(graph):
    index = 0
    stack = []
    indices = {}
    lowLinks = {}
    onStack = set()
    sccs = []

    function StrongConnect(node):
        indices[node] = index
        lowLinks[node] = index
        index += 1
        stack.push(node)
        onStack.add(node)

        for neighbor in graph[node]:
            if neighbor not in indices:
                StrongConnect(neighbor)
                lowLinks[node] = min(lowLinks[node], lowLinks[neighbor])
            elif neighbor in onStack:
                lowLinks[node] = min(lowLinks[node], indices[neighbor])

        if lowLinks[node] == indices[node]:
            scc = []
            while True:
                w = stack.pop()
                onStack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in indices:
            StrongConnect(node)

    return sccs
```
