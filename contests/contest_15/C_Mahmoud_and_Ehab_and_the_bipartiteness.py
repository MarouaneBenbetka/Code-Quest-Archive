from collections import defaultdict
import sys
import threading

n = int(input())

graph = defaultdict(list)


for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

blue = 0
red = 0

colors = [0]*(n+1)


def dfs(node, color):
    global blue
    global red
    colors[node] = color
    if color == 1:
        blue += 1
    else:
        red += 1
    for child in graph[node]:
        if colors[child] == 0:
            dfs(child, 3-color)


def main():

    dfs(1, 1)

    ans = 0
    for node in graph:
        if colors[node] == 1:
            ans += red - len(graph[node])
        else:
            ans += blue - len(graph[node])

    print(ans//2)


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
