
from collections import deque


for _ in range(int(input())):
    n, k = map(int, input().split())

    costs = list(map(int, input().split()))

    unlimited_potions = [potion-1 for potion in map(int, input().split())]

    for unlimited_potion in unlimited_potions:
        costs[unlimited_potion] = 0

    # print(costs)

    graph = [[] for _ in range(n)]

    in_degree = [0]*n
    for node in range(n):
        components = list(map(int, input().split()))

        if components[0] == 0:
            continue
        for i in range(1, len(components)):
            graph[node].append(components[i]-1)
            in_degree[components[i]-1] += 1
    # print(graph)
    queue = deque()
    for node in range(n):
        if in_degree[node] == 0:
            queue.append(node)

    top_sort_potions = deque()

    while queue:
        potion = queue.popleft()
        top_sort_potions.appendleft(potion)

        for neighbor in graph[potion]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    # print(top_sort_potions)

    for potion in top_sort_potions:

        ssum = 0
        for neighbor in graph[potion]:
            ssum += costs[neighbor]

        if graph[potion]:
            costs[potion] = min(costs[potion], ssum)

    print(*costs)
