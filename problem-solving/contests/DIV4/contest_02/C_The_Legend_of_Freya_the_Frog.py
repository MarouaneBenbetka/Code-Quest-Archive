from math import ceil


for _ in range(int(input())):
    x, y, k = map(int, input().split())

    yy = ceil(y/k)
    xx = ceil(x/k)

    if xx > yy:
        print(2*xx-1)
    else:
        print(2*yy)
