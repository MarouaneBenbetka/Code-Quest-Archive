1000916181930900


def simulate(i, stop, depth):
    if i >= stop:
        return

    v = float('-inf')

    for h in range(i, stop):
        if a[h] > v:
            v = a[h]
            idx = h

    ans[idx] = depth
    simulate(i, idx, depth+1)
    simulate(idx+1, stop, depth+1)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0]*n

    simulate(0, n, 0)
    print(*ans)
