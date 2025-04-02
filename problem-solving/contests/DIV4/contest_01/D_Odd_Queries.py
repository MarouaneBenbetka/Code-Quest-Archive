

for _ in range(int(input())):
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))

    pfx = [0] * (n + 1)

    for i in range(1, n + 1):
        pfx[i] = pfx[i - 1] + nums[i - 1]

    for _ in range(q):
        l, r, k = map(int, input().split())

        if (pfx[n] - (pfx[r]-pfx[l-1]) + k * (r-l+1)) % 2:
            print("YES")
        else:
            print("NO")
