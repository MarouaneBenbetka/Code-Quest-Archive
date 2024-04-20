

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    mp = {}
    ans = 0
    for i in range(n):
        p = a[i] % x
        q = a[i] % y
        val = x - p if p != 0 else 0
        ans += mp.get((val, q), 0)
        mp[(p, q)] = mp.get((p, q), 0) + 1

    print(ans)
