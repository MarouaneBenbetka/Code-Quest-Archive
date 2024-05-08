

def get2s(x):
    total = 0
    while x % 2 == 0:
        x //= 2
        total += 1
    return total


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    x = 0
    b = []

    for i in range(n):
        x += get2s(a[i])
        b.append(get2s(i + 1))

    if x >= n:
        print(0)
    else:
        cpt = 0
        b.sort(reverse=True)

        for i in b:
            cpt += 1
            if x + i >= n:
                break
            x += i
        else:
            cpt = -1

        print(cpt)
