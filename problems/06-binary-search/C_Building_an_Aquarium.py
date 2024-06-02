import math


def check_valid_height(a,  x, mid):
    cpt = 0
    for col in a:
        cpt += max(0, mid - col)

    return cpt <= x


for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    low = 1
    high = math.ceil(x+max(a)+1)

    cpt = 0
    while low < high - 1:
        cpt += 1
        mid = low + (high - low)//2

        if check_valid_height(a, x, mid):
            low = mid
        else:
            high = mid

    print(low)
