for _ in range(int(input())):
    n = int(input())
    a = [c for c in input()]

    b = []
    c = m = ''
    i = len(a)
    while i:
        i -= 1
        if a[i] >= m:
            m = a[i]
            b += [i]
            c += m
    for x in c:
        a[b.pop()] = x
    print((len(c.strip(c[-1])), -1)[a > sorted(a)])
