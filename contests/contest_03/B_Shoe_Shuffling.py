t = int(input())

for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    v.append(10**9 + 1)
    size = 1
    start = 0
    can = True
    w = []

    for p in range(1, n + 1):
        if v[p] == v[p - 1]:
            size += 1
            continue
        if size == 1:
            can = False
            break
        w.append(p)
        w.extend(range(start+1, p))
        start = p
        size = 1

    if can:
        print(*w)
    else:
        print("-1")
