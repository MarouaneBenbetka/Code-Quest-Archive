from collections import Counter, defaultdict


n = int(input())
masses = list(map(int, input().split()))

maxx = max(masses)

cnt = Counter(masses)


dp = defaultdict(int)


for mass in range(maxx + 1):
    dp[mass] = max(dp[mass-1], dp[mass-2] + cnt[mass]*mass)

print(dp[maxx])
