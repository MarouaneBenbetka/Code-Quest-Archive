from collections import Counter


for _ in range(int(input())):
    n, m, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt1 = Counter()
    for i in range(m):
        cnt1[a[i]] += 1
    cnt2 = Counter(b)

    ans = 0
    curr = 0

    for value in cnt1:
        v1 = cnt1[value]
        v2 = cnt2[value]
        curr += min(v1, v2)

        if n == m and cnt1[value] != cnt2[value]:
            ans = 0
            break

    if curr >= k:
        ans += 1

    for i in range(n-m):

        old = min(cnt1[a[i]], cnt2[a[i]])
        cnt1[a[i]] -= 1
        new = min(cnt1[a[i]], cnt2[a[i]])

        if new > old:
            curr += 1
        elif new < old:
            curr -= 1

        old = min(cnt1[a[i+m]], cnt2[a[i+m]])
        cnt1[a[i+m]] += 1
        new = min(cnt1[a[i+m]], cnt2[a[i+m]])

        if new > old:
            curr += 1
        elif new < old:
            curr -= 1

        if curr >= k:
            ans += 1

    print(ans)
