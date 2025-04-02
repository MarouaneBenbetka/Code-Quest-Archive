
for _ in range(int(input())):
    n = int(input())

    nums = sorted(list(map(int, input().split())))

    if nums[0] != 1:
        print("NO")
        continue

    _sum = 1

    for i in range(1, n):
        if nums[i] > _sum:
            print("NO")
            break
        else:
            _sum += nums[i]
    else:
        print("YES")
