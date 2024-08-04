
from collections import deque


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False]*n


def bfs(strt):
    queue = deque([strt])
    visited[strt] = True
    is_cycle = True

    while queue:
        node = queue.popleft()

        if len(graph[node]) != 2:
            is_cycle = False

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return is_cycle


cpt = 0
for node in range(n):
    if not visited[node]:
        if bfs(node):
            cpt += 1

print(cpt)
