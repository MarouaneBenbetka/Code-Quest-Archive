n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
best = 0
best_index = -1

for i in range(n):
    sum_val = a[i]
    cmax = a[i]

    for j in range(i + 1, n):
        cmax = min(cmax, a[j])
        sum_val += cmax

    cmax = a[i]

    for j in range(i - 1, -1, -1):
        cmax = min(cmax, a[j])
        sum_val += cmax

    if sum_val > best:
        best = sum_val
        best_index = i

if best_index != -1:
    cmax = a[best_index]
    ans[best_index] = cmax

    for j in range(best_index + 1, n):
        cmax = min(cmax, a[j])
        ans[j] = cmax

    cmax = a[best_index]

    for j in range(best_index - 1, -1, -1):
        cmax = min(cmax, a[j])
        ans[j] = cmax

print(*ans)
