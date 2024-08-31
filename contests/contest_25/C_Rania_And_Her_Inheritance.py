from collections import defaultdict
import sys
import threading

best_team_size = 0
best_team = []


def main():
    def backtrack(index, curr, state):
        global best_team, best_team_size

        if index == n:
            if len(curr) > best_team_size:
                best_team_size = len(curr)
                best_team = curr.copy()
            return

        if (state & (1 << index)) == 0:
            for member in curr:
                if names[index] in graph[member]:
                    break
            else:
                curr.append(names[index])
                backtrack(index + 1, curr, state | (1 << index))
                curr.pop()

        backtrack(index + 1, curr, state)

    n, m = map(int, input().split())
    names = []
    graph = defaultdict(list)

    for i in range(n):
        names.append(input())

    for _ in range(m):
        expert1, expert2 = input().split()
        graph[expert1].append(expert2)
        graph[expert2].append(expert1)

    initial_state = 0  # trivial ones
    trivial_team = []
    for i in range(n):
        if not graph[names[i]]:
            trivial_team.append(names[i])
            initial_state |= (1 << i)

    backtrack(0, trivial_team, initial_state)

    print(best_team_size)
    best_team.sort()
    print(*best_team, sep='\n')


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
