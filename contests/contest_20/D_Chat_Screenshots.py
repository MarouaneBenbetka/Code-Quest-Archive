import sys
import threading


def dfs(node, state, graph):
    # 1 for visited
    # -1 for visiting

    if state[node] == -1:
        return False

    if state[node] == 1:
        return True

    state[node] = -1

    for child in graph[node]:
        if not dfs(child, state, graph):
            return False

    state[node] = 1

    return True


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())

        orders = [[] for _ in range(n)]
        state = [0 for _ in range(n)]
        for __ in range(k):
            order = list(map(int, input().split()))

            for i in range(1, n-1):
                orders[order[i]-1].append(order[i+1]-1)

        # print(orders)

        for i in range(n):
            if not dfs(i, state, orders):
                print("NO")
                break
        else:
            print("YES")


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
