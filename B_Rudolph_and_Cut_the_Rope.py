
for _ in range(int(input())):
    n = int(input())
    heights = []
    ropes = []

    cpt = 0
    for _ in range(n):
        a, b = map(int, input().split())

        if b < a:
            cpt += 1

    print(cpt)
