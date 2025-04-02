from collections import deque


for _ in range(int(input())):

    n, m, k, d = map(int, input().split())

    ans = []

    for _ in range(n):
        row = list(map(int, input().split()))

        dp = [0]*(m)
        dp[0] = row[0]+1

        d_previous_cells = deque([0])

        for j in range(1, m):
            dp[j] = row[j] + dp[d_previous_cells[0]]+1

            while d_previous_cells and dp[j] < dp[d_previous_cells[-1]]:
                d_previous_cells.pop()
            d_previous_cells.append(j)

            if j - d_previous_cells[0] > d:
                d_previous_cells.popleft()

        ans.append(dp[-1])

    left = 0
    window = 0

    res = float('inf')
    for right in range(n):
        window += ans[right]

        if right >= k:
            window -= ans[left]
            left += 1

        if right - left + 1 >= k:
            res = min(res, window)

    print(res)
