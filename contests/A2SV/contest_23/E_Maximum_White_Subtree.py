import sys
import threading

n = 0
graph = []
down_dp = []
parent = []
colors = []
up_dp = []


def dfs1(node):
    down_dp[node] = colors[node]
    for child in graph[node]:
        if child == parent[node]:
            continue
        parent[child] = node
        dfs1(child)
        down_dp[node] += max(down_dp[child], 0)


def dfs2(node):
    for child in graph[node]:
        if child == parent[node]:
            continue
        up_dp[child] = max(
            down_dp[node] - max(down_dp[child], 0) + up_dp[node], 0)
        dfs2(child)


def main():
    global n, graph, down_dp, parent, colors, up_dp
    n = int(input())

    graph = [[] for _ in range(n)]
    down_dp = [0] * n
    parent = [0] * n
    up_dp = [0] * n

    colors = list(map(int, input().replace('0', '-1').split()))

    for _ in range(n-1):
        in1, in2 = map(int, input().split())
        graph[in1-1].append(in2-1)
        graph[in2-1].append(in1-1)

    dfs1(0)
    dfs2(0)

    for i in range(n):
        print(down_dp[i] + up_dp[i], end=" ")


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
