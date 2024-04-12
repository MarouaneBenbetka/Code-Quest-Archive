# https://leetcode.com/problems/max-consecutive-ones-iii/
arr = list(map(int, input().split()))
n = len(arr)

can_skip = int(input())

i = 0

max_index = 0
max_count = 0

curr_max_count = 0
while i < n:
    if arr[i] == 1:
        curr_max_count += 1
        i += 1
    elif arr[i] == 0:
        if not can_skip:
            if curr_max_count > max_count:
                max_count = curr_max_count
                max_index = i

            j = i - curr_max_count
            while arr[j] != 0:
                j += 1
                curr_max_count -= 1

            j += 1
            curr_max_count -= 1
            can_skip += 1

        else:

            can_skip -= 1
            curr_max_count += 1
            i += 1

if curr_max_count > max_count:
    max_count = curr_max_count
    max_index = i

print(max_count)
