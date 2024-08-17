input()

nums = list(map(int, input().split()))

prev = 0
best = 0
curr = 0
for num in nums:
    if num > prev:
        curr += 1
    else:
        curr = 1

    if curr > best:
        best = curr

    prev = num


print(best)
