
from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    y = 0
    x = 0
    for node in graph:
        if len(graph[node]) == 1:
            second_node = graph[node][0]
            y = len(graph[second_node])-1

            for third_node in graph[second_node]:
                if len(graph[third_node]) > 1:
                    x = len(graph[third_node])
                    break

    print(x, y)
