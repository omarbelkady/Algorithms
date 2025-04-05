Algorithm BellmanFord(Graph, source):
'''pseudo
<br/>
    Input: 
<br/>
       Graph = (V, E) where V is the set of vertices and E is the set of edges with weight w
        <br/>source: the starting vertex
<br/>
    Output:
<br/>
<br/>

  distance[]: array of shortest distances from source to each vertex
<br/>
        OR an indication that a negative weight cycle exists
<br/>
<br/>
   Step 1: Initialize distances
<br/>
<br/>
    for each vertex v in V do:
<br/>
        if v == source then
<br/>
<br/>
            distance[v] ← 0
<br/>
<br/>
        else
<br/>
<br/>
            distance[v] ← ∞
<br/>
<br/>
        end if
<br/>
<br/>
    end for
<br/>
         Step 2: Relax all edges |V| - 1 times
<br/>
<br/>
    for i from 1 to |V| - 1 do:
<br/>
<br/>
        for each edge (u, v) in E do:
<br/>
            if distance[u] + weight(u, v) < distance[v] then:
<br/>
<br/>
                distance[v] ← distance[u] + weight(u, v)
<br/>
            end if
<br/>
<br/>
        end for
<br/>
<br/>
    end for
<br/>
    // Step 3: Check for negative-weight cycles
<br/>
<br/>
    for each edge (u, v) in E do:
<br/>
<br/>
        if distance[u] + weight(u, v) < distance[v] then:
<br/>
<br/>
            print("Graph contains a negative weight cycle")
<br/>
<br/>
            return "Negative cycle detected"
<br/>
<br/>
        end if
<br/>
<br/>
    end for
<br/>
    return distance
