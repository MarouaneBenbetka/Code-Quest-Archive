from collections import defaultdict
import sys
import threading


def main():
    for _ in range(int(input())):
        n = int(input())
        nodes = list(map(int, input().split()))
        parents = list(map(int, input().split()))

        graph = [[] for _ in range(n + 1)]
        for i in range(1, n):
            graph[parents[i - 1]].append(i + 1)
            stack = [(1, None)]

        results = [0] * (n + 1)
        visited = [False] * (n + 1)
        min_values = [float('inf')] * (n + 1)

        while stack:
            node, parent = stack[-1]

            if not visited[node]:
                visited[node] = True
                is_leaf = True
                for neighbor in graph[node]:
                    if neighbor != parent:
                        stack.append((neighbor, node))
                        is_leaf = False

                if is_leaf:
                    results[node] = nodes[node - 1]
                    min_values[node] = results[node]
                else:
                    continue

            stack.pop()
            if parent is None:
                results[node] = nodes[node - 1] + min_values[node]
            else:
                results[node] = min(
                    (nodes[node - 1] + min_values[node]) // 2, min_values[node])
                min_values[parent] = min(min_values[parent], results[node])

        print(results[1])


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
