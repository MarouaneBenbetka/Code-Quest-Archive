
for _ in range(int(input())):

    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort(reverse=True)

    print(sum(nums[:n//2+1]))
