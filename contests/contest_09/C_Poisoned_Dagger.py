

k = 10**18

k = 0
k = 1


k = [0, 1, 2, 3, 4, 5, 6, 7, ..., 10**18]


def check_valid(arr, k, h):
    s = 0
    for i in range(1, len(arr)):
        if s >= h:
            return True
        if arr[i] - arr[i - 1] >= k:
            s += k
        else:
            s += (arr[i] - arr[i - 1])
    if s + k >= h:
        return True
    return False


for _ in range(int(input())):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    l, r = 0, 10**18
    res = None

    while l <= r:
        mid = (r + l) // 2
        if check_valid(arr, mid, h):
            r = mid - 1
            res = mid
        else:
            l = mid + 1

    print(res)
