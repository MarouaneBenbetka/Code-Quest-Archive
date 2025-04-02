

for _ in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))

    nums.sort()

    if nums[0] != 1:
        print("NO")
        continue

    # 1 1 2 3 5
    # 1 1 2 5 7
    # 1 1 1
    # 1 1 1 2 4
    # 1 1 2 3 4 7
    curr = 1
    for i in range(1, n):
        if nums[i] > curr:
            print("NO")
            break

        curr += nums[i]
    else:
        print("YES")
