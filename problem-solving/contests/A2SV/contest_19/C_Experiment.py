n = int(input())
log = []

for i in range(n):
    s, t, b = map(int, input().split())
    log.append((s, b))
    log.append((t+1, -b))

log.sort()


ans = 0
curr = 0

for _, rooms in log:
    curr += rooms
    ans = max(ans, curr)

print(ans)
