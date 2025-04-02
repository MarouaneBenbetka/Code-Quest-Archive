
from collections import defaultdict

for _ in range(int(input())):

    n, m = map(int, input().split())

    skip = defaultdict(set)

    for _ in range(m):
        x, y = map(int, input().split())
        skip[y].add(x)

    answer = [i for i in range(1, n+1)]

    for i in range(1, n+1):

        left = i-2

        while left >= 0 and answer[left] in skip[i]:
            answer[left], answer[left+1] = answer[left+1], answer[left]
            left -= 1

    print(*answer)
