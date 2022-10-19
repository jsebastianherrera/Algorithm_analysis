import random
import sys
import networkx as nx


def aprox(g: nx.Graph, n: int):
    visited = [False] * (n)
    for u in range(n):
        if not visited[u]:
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    visited[u] = True
                    break

    # Print the vertex cover
    for j in range(n):
        if visited[j]:
            print(j, end=' ')


# Read data
if len(sys.argv) < 4:
    print("Usage: python3", sys.argv[0], "n p d")
    sys.exit(1)
# end if
n = int(sys.argv[1])
p = float(sys.argv[2])
d = bool(sys.argv[3])

g = nx.Graph()
# Show results
for i in range(n):
    for j in range(n):
        if i != j:
            q = random.uniform(0, 1)
            if q < p:
                g.add_edge(i, j)
            # end if
        # end if
    # end for
# end for
aprox(g, n)
