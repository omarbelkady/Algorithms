```plaintext
function Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]

function Union(parent, rank, x, y):
    rootX = Find(parent, x)
    rootY = Find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
```