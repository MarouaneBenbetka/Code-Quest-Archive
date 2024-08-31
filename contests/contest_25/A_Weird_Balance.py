

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort(reverse=True)

    first = nums[0]

    curr = 1
    while curr < n and nums[curr] == first:
        curr += 1

    if curr == n:
        print("NO")
        continue

    nums[0] = nums[curr]
    nums[curr] = first

    print("YES")
    print(*nums)
