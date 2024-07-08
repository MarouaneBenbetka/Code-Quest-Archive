from collections import defaultdict, deque

n, t = map(int, input().split())


arr = list(map(int, input().split()))


graph = defaultdict(list)

for i, a in enumerate(arr):
    graph[i+1].append(a+i+1)


queue = deque([1])
visited = [False]*(n+1)

while queue:

    node = queue.popleft()
    visited[node-1] = True

    for neighbor in graph[node]:
        if neighbor == t:
            print("YES")
            exit()

        if not visited[neighbor-1]:
            queue.append(neighbor)

print("NO")
