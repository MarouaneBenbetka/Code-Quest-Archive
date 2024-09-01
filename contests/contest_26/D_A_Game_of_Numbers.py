

for _ in range(int(input())):
    n, m = map(int, input().split())

    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    nums1.sort()
    nums2.sort()

    p1_left = 0
    p1_right = n-1

    p2_left = 0
    p2_right = m-1

    diff = 0

    while p1_left <= p1_right:

        option1 = abs(nums1[p1_left] - nums2[p2_right])
        option2 = abs(nums1[p1_right] - nums2[p2_left])

        if option1 > option2:
            diff += option1
            p1_left += 1
            p2_right -= 1
        else:
            diff += option2
            p1_right -= 1
            p2_left += 1

    print(diff)
