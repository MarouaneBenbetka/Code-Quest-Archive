max_val = 1000000  # Update this with the actual known maximum value if needed

cnt_b = [0] * (max_val + 1)

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    a = list(map(int, input().split()))  # n elements
    b = list(map(int, input().split()))  # m elements

    for i in range(m):
        cnt_b[b[i]] += 1

    b_values = set(b)

    ans = 0
    curr = 0

    for i in range(m):
        if a[i] in b_values:
            cnt_b[a[i]] -= 1
            if cnt_b[a[i]] >= 0:
                curr += 1

    if curr >= k:
        ans += 1

    for i in range(n - m):
        if a[i] in b_values:
            cnt_b[a[i]] += 1
            if cnt_b[a[i]] > 0:
                curr -= 1

        if a[i + m] in b_values:
            cnt_b[a[i + m]] -= 1
            if cnt_b[a[i + m]] >= 0:
                curr += 1

        if curr >= k:
            ans += 1

    print(ans)

    for i in b_values:
        cnt_b[i] = 0
