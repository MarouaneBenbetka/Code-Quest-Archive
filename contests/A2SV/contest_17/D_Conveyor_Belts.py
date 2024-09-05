

for _ in range(int(input())):
    n, x1, y1, x2, y2 = map(int, input().split())

    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    a1 = min(x1, n-x1-1)
    b1 = min(y1, n-y1-1)
    c1 = min(a1, b1)

    d1 = min(x2, n-x2-1)
    e1 = min(y2, n-y2-1)
    f1 = min(d1, e1)

    print(abs(c1-f1))
