from collections import defaultdict
import sys
import threading


def main():

    n, m = map(int, input().split())

    has_cat = list(map(int, input().split()))

    graph = defaultdict(list)

    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(n)

    def dfs(node, cat_count):

        visited[node-1] = True

        if has_cat[node-1]:
            cat_count += 1
        else:
            cat_count = 0

        if cat_count > m:
            return 0

        if len(graph[node]) == 1 and node != 1:
            return 1

        ans = 0

        for neighbor in graph[node]:
            if not visited[neighbor-1]:
                ans += dfs(neighbor, cat_count)

        return ans
    print(dfs(1, 0))


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
