

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            sum_val = a[i][j]
            x = j - 1
            y = j + 1
            for k in range(i - 1, -1, -1):
                if x >= 0:
                    sum_val += a[k][x]
                    x -= 1
                if y < m:
                    sum_val += a[k][y]
                    y += 1
            x = j - 1
            y = j + 1
            for k in range(i + 1, n):
                if x >= 0:
                    sum_val += a[k][x]
                    x -= 1
                if y < m:
                    sum_val += a[k][y]
                    y += 1
            if sum_val > ans:
                ans = sum_val
    print(ans)
