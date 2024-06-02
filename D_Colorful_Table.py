
results = []

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sl = [n + 1] * (k + 1)
    sr = [-1] * (k + 1)
    se = set(a)

    for i in range(n):
        sl[a[i]] = min(sl[a[i]], i)
        sr[a[i]] = i

    for i in range(1, k):
        sl[i] = min(sl[i], sl[i - 1])
        sr[i] = max(sr[i], sr[i - 1])

    result = []
    for i in range(0, k):
        if i not in se:
            result.append("0")
        else:
            result.append(str(2 * (sr[i] - sl[i] + 1)))

    print(" ".join(result))
