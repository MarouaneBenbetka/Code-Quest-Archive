
from collections import deque
import sys
import threading


def dfs(node, visited, graph, costs):

    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, visited, graph, costs)

        if graph[node]:
            ssum = 0
            for neighbor in graph[node]:
                ssum += costs[neighbor]
            costs[node] = min(costs[node], ssum)


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())

        costs = list(map(int, input().split()))

        unlimited_potions = [potion-1 for potion in map(int, input().split())]

        for unlimited_potion in unlimited_potions:
            costs[unlimited_potion] = 0

        # print(costs)

        graph = [[] for _ in range(n)]

        for node in range(n):
            components = list(map(int, input().split()))

            if components[0] == 0:
                continue
            for i in range(1, len(components)):
                graph[node].append(components[i]-1)

        visited = [False]*n

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node, visited, graph, costs)

        print(*costs)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
