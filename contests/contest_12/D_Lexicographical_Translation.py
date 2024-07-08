from collections import Counter, deque

s = input()


cnt = Counter(s)


t = deque()
u = deque()


for c in s:
    t.append(c)
    cnt[c] -= 1

    if cnt[c] == 0:
        del cnt[c]

    while t and all(t[-1] <= ch for ch in cnt):
        u.append(t.pop())

while t:
    u.append(t.pop())

print(*u, sep='')
