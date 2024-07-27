n = int(input())
maxx = 100001
log = [0]*maxx

for i in range(n):
    s, t, b = map(int, input().split())
    log[s] += b
    log[t + 1] -= b

ans = 0
cur = 0

for i in range(maxx):
    cur += log[i]
    if cur > ans:
        ans = cur

print(ans)
