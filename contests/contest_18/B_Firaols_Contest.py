
from collections import defaultdict
n, m = map(int, input().split())


problems_diff = list(map(int, input().split()))


curr = defaultdict(lambda: 0)

for problem in problems_diff:
    curr[problem] += 1

    if len(curr) == n:
        print(1, end="")
        for i in range(1, n+1):
            curr[i] -= 1
            if curr[i] == 0:
                del curr[i]
    else:
        print(0, end="")
print()
