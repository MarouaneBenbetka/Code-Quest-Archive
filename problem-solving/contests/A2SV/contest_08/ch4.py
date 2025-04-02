
from collections import deque

# horse array

n = int(input())

horse_prices = list(set(int(input()) for _ in range(n)))

morgan_budget = int(input())

nb_horses_need_purchase = int(input())


horse_prices.sort()
q = deque([(0, 0, [])])
res = []
while q:
    cost, i, horses = q.popleft()
    if len(horses) == nb_horses_need_purchase:
        if cost == morgan_budget:
            res += [horses]
    elif i < len(horse_prices):
        q.append((cost, i + 1, horses))
        q.append((cost + horse_prices[i], i +
                  1, horses + [horse_prices[i]]))

print(sorted(res))
