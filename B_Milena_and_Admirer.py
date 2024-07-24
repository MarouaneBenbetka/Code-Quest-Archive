

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    cpt = 0

    for i in range(n-2, -1, -1):
        if nums[i] > nums[i+1]:
            q, r = divmod(nums[i], nums[i+1])

            cpt += q-1

            if r == 0:
                nums[i] = nums[i+1]
            else:
                cpt += 1
                nums[i] = (nums[i])//(q+1)

    print(cpt)
