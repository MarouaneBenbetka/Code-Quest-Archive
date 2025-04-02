n, k, p = (map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

best = float('inf')
for key in range(k-n+1):
    ans = float('-inf')
    for offset in range(n):
        ans = max(ans, abs(a[offset] - b[key+offset]) + abs(b[key+offset] - p))
    best = min(best, ans)
print(best)
