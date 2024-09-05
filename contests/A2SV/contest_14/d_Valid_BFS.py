from collections import defaultdict, deque

n = int(input())

graph = defaultdict(list)

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs_to_check = list(map(int, input().split()))

order = defaultdict(int)
for i in range(len(bfs_to_check)):
    order[bfs_to_check[i]] = i+1

for src in graph:
    graph[src].sort(key=lambda x: order[x])

queue = deque([1])


tmp = []
visited = [False] * (n+1)
visited[1] = True
while queue:

    node = queue.popleft()
    tmp.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)


if tmp == bfs_to_check:
    print("Yes")
else:
    print("No")
