

for _ in range(int(input())):
    n = int(input())

    piles = list(map(int, input().split()))

    pfx = [0] * (n + 1)
    for i in range(1, n + 1):
        pfx[i] = pfx[i - 1] + piles[i - 1]

    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2
        expected = pfx[mid+1] - pfx[left]

        print(f"? {mid - left +1}", *range(left+1, mid+2))

        if int(input()) == expected:
            left = mid + 1
        else:
            right = mid

    print(f"! {left+1}")
