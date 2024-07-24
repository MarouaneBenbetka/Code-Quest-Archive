

n = int(input())


nums = list(map(int, input().split()))
nums.sort()

break_point = 0

left_part = sum(nums[:n])
right_part = sum(nums[n:])

if left_part == right_part:
    print(-1)
else:
    print(*nums)
