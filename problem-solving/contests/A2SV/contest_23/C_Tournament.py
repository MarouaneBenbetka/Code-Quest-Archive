

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        produce = list(map(int, input().split()))

        max_halfs = max(produce).bit_length()+1

        dp = [[0] * (max_halfs + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for h in range(max_halfs):
                current_produce = produce[i] // (2 ** h)
                full_pick = current_produce - k + dp[i + 1][h]
                half_pick = (current_produce // 2) + dp[i + 1][h + 1]

                dp[i][h] = max(full_pick, half_pick)

        print(dp[0][0])


main()
