for _ in range(int(input())):
    n = int(input())

    points = set(tuple(map(int, input().split())) for _ in range(n))

    cpt = 0
    for x, y in points:

        if y == 0 and (x, 1) in points:
            cpt += n - 2

        if (x-1, 1-y) in points and (x+1, 1-y) in points:
            cpt += 1

    print(cpt)
