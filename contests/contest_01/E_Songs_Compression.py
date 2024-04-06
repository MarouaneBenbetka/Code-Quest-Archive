
n, m = map(int, input().split())
a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

diff = [b[i] - a[i] for i in range(n)]
total = sum(a)
diff.sort()
i = 0
while total > m and i < n:
    total += diff[i]
    i += 1
print(i if total <= m else -1)
