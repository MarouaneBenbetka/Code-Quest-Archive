
for _ in range(int(input())):

    n = int(input())
    seq = list(map(int, input().split()))

    reachable = set([0])

    for i in range(n):

        # left flag
        if i - seq[i] >= 0 and i - seq[i] in reachable:
            reachable.add(i+1)

        # right flag
        if i in reachable and i + seq[i] < n:
            reachable.add(i + seq[i]+1)

    print("YES" if n in reachable else "NO")
