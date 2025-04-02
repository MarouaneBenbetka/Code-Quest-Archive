
for _ in range(int(input())):

    n = int(input())

    nums = map(int, input().split())

    sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])

    pfx = [0] * n
    dp = [0] * n
    score = 0

    for i in range(n):
        score += sorted_nums[i][0]
        pfx[i] = score

    for i in range(n-1, -1, -1):

        if i < n-1 and pfx[i] >= sorted_nums[i+1][0]:
            dp[i] = dp[i+1]
        else:
            dp[i] = i

    ans = [0]*n
    for i in range(n):
        ans[sorted_nums[i][1]] = dp[i]

    print(*ans)
