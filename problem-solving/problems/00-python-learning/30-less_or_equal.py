# https://codeforces.com/problemset/problem/977/C


n, k = map(int, input().split())
a = sorted(map(int, input().split()))


if k == 0 and a[0] > 1:
    print("1")
elif k == 0 and a[0] == 1:
    print("-1")
elif k <= n - 1:
    if a[k - 1] != a[k]:
        print(a[k - 1])
    else:
        print("-1")
elif k == n:
    print(a[k - 1])
