from collections import deque

for _ in range(int(input())):
    n = int(input())

    res = deque()

    for _ in range(n):
        res.appendleft(input().index("#")+1)

    print(*res)
