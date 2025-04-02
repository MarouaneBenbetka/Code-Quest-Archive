from collections import defaultdict

n, edges = map(int, input().split())


graph = defaultdict(list)

for _ in range(edges):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


lens = [len(graph[i]) for i in range(1, n+1)]

possible_lens = list(set(lens))

if len(possible_lens) == 1 and lens[0] == 2:
    print('ring topology')
    exit()

if len(possible_lens) == 2 and lens.count(1) == 2 and 2 in possible_lens:
    print('bus topology')
    exit()

if len(possible_lens) == 2 and lens.count(n-1) == 1 and lens.count(1) == n-1:
    print('star topology')
    exit()

print('unknown topology')
