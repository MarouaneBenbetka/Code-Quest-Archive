for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    left = 0
    right = 0

    res = 0
    while right < n:

        while right < n and (a[left] < 0 and a[right] < 0 or a[left] > 0 and a[right] > 0):
            if a[right] > a[left]:
                left = right
            right += 1

        res += a[left]
        left = right

    print(res)
