for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)

    left = 1
    right = n+1

    while left != right - 1:
        mid = (left + right) // 2

        if a[mid] > x:
            right = mid
        else:
            left = mid

    if a[left] == x:
        print(0)
    else:
        print(1)
        print(a.index(x), left)
