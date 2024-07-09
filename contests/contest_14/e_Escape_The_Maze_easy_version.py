
from collections import defaultdict, deque
import sys
import threading


def main():
    x = int(input())

    for _ in range(x):
        input()
        n_rooms, n_friends = map(int, input().split())

        rooms_with_friends = set(map(int, input().split()))

        graph = defaultdict(list)
        for i in range(n_rooms-1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        dist = [-1]*(n_rooms+1)

        queue = deque(rooms_with_friends)
        for friend in rooms_with_friends:
            dist[friend] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

        def dfs(node, parent, d):
            if d >= dist[node]:
                return False

            if parent != -1 and len(graph[node]) == 1:
                return True

            for neighbor in graph[node]:
                if neighbor != parent:
                    if dfs(neighbor, node, d+1):
                        return True

            return False

        if dfs(1, -1, 0):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
