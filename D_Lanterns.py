

for _ in range(int(input())):
    n = int(input())

    lanterns = []

    for i in range(n):
        a, b = map(int, input().split())
        lanterns.append((a, -b))

    lanterns.sort()

    ans = 0
    on = 0
    i = 0
    start = 0

    while i < n:
        ans -= lanterns[i][1]
        on += 1
        i += 1
        cnt = 0

        while start < n and lanterns[start][0] <= on:
            if start < i:
                cnt += 1
            start += 1

        on -= cnt
        i = max(i, start)

    print(ans)
