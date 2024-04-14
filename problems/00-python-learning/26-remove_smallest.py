
# https://codeforces.com/problemset/problem/1399/A
for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))

    for i in range(n-1):
        if arr[i+1] - arr[i] > 1:
            print('NO')
            break
    else:
        print('YES')
