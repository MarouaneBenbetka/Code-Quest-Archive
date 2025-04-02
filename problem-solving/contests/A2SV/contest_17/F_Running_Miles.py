

for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))

    pfx = [0] * (n + 1)
    sfx = [float('-inf')] * (n+1)

    for i in range(1, n + 1):
        pfx[i] = max(pfx[i - 1], + arr[i - 1] + i-1)

    for i in range(n-1, -1, -1):
        sfx[i] = max(sfx[i + 1], arr[i] - i)

    ans = 0

    for i in range(1, n-1):
        ans = max(ans, pfx[i] + arr[i] + sfx[i+1])

    print(ans)
