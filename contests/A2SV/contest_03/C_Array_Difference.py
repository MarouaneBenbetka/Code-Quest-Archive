

for _ in range(int(input())):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a = sorted(a_list)
    b = sorted(b_list, reverse=True)

    d = 0

    right = -1

    left = 0
    break_flag = -1
    for i in range(n):
        if abs(a[i] - b[-(n-i)]) > abs(a[i] - b[i]):
            break_flag = i
            break
        d += abs(a[i] - b[i])

    if break_flag != -1:
        for i in range(break_flag, n):
            d += abs(a[i] - b[-(n-i)])

    print(d)
