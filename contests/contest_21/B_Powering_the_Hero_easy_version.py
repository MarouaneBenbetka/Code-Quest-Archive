
from heapq import heappush, heappop

for _ in range(int(input())):

    n = int(input())

    heap = []

    power = 0

    cards = list(map(int, input().split()))
    for card in cards:

        if card == 0:
            if heap:
                power -= heappop(heap)
        else:
            heappush(heap, -card)

    print(power)
