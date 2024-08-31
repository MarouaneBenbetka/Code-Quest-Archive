from bisect import bisect_right

for _ in range(int(input())):

    n, s = map(int, input().split())

    times = list(map(int, input().split()))

    total = sum(times)

    if total <= s:
        print(0)
        continue

    pfx = [0] * (n + 1)
    for j in range(1, n + 1):
        pfx[j] = pfx[j - 1] + times[j - 1]

    if pfx[n] <= s:
        print(0)
        continue

    best_skip = 1
    max_completed = 0

    for j in range(n):

        if pfx[j] > s:
            break
        max_possible = max_possible = bisect_right(pfx, s + times[j]) - 1

        if max_possible > max_completed:
            max_completed = max_possible
            best_skip = j + 1

    print(best_skip)
