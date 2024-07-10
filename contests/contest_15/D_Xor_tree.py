from collections import defaultdict
import sys
import threading


n = int(input())

graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


given = list(map(int, input().split()))
gaol = list(map(int, input().split()))

visited = [False]*(n+1)

res = []


def dfs(node, odd, even):
    global res
    visited[node] = True

    if given[node-1] ^ odd != gaol[node-1]:
        res.append(node)
        odd ^= 1

    for child in graph[node]:
        if not visited[child]:
            dfs(child, even, odd)


def main():
    dfs(1, 0, 0)
    print(len(res))
    print(*res, sep='\n')


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
