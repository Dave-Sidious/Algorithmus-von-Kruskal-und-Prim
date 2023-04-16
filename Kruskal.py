def kruskal_mst(graph):
    parent = {}
    rank = {}
    mst = []

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                if rank[root1] == rank[root2]:
                    rank[root1] += 1

    for node in graph:
        parent[node] = node
        rank[node] = 0

    edges = [(graph[u][v], u, v) for u in graph for v in graph[u]]
    edges.sort()

    for cost, frm, to in edges:
        if find(frm) != find(to):
            union(frm, to)
            mst.append((frm, to, cost))

    return mst

graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

mst = kruskal_mst(graph)
print(mst)