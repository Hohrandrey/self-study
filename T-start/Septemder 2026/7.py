"""
5 6
1 2 10
2 3 8
3 4 6
4 5 4
1 3 5
2 5 7
1 5 6
1 4 3
2 4 2
3 5 1
"""
#Изучить
from collections import deque


n, q = map(int, input().split())

adj = [[] for _ in range(n + 1)]
edges = []

total = 0
for i in range(n - 1):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    adj[a].append((b, c, i))
    adj[b].append((a, c, i))
    total += c

out = []

for _ in range(q):
    u, v, w = map(int, input().split())

    parent = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)
    visited = [False] * (n + 1)

    queue = deque([u])
    visited[u] = True

    while queue:
        cur = queue.popleft()
        if cur == v:
            break
        for neighbor, weight, eid in adj[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = cur
                parent_edge[neighbor] = eid
                queue.append(neighbor)

    max_weight = 0
    max_eid = -1
    cur = v
    while cur != u:
        eid = parent_edge[cur]
        ew = edges[eid][2]
        if ew > max_weight:
            max_weight = ew
            max_eid = eid
        cur = parent[cur]

    if w < max_weight:
        old_a, old_b, old_c = edges[max_eid]

        adj[old_a] = [(nb, wt, ei) for nb, wt, ei in adj[old_a] if ei != max_eid]
        adj[old_b] = [(nb, wt, ei) for nb, wt, ei in adj[old_b] if ei != max_eid]

        new_eid = len(edges)
        edges.append((u, v, w))
        adj[u].append((v, w, new_eid))
        adj[v].append((u, w, new_eid))

        total += w - max_weight

    out.append(str(total))

print('\n'.join(out))
