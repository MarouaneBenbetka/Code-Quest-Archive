from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)


for _ in range(n):
    dest, _, src = input().split()

    graph[src.lower()].append(dest.lower())

queue = deque(["polycarp"])

lvl = 0

while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        for neighbor in graph[node]:
            queue.append(neighbor)
    lvl += 1

print(lvl)
