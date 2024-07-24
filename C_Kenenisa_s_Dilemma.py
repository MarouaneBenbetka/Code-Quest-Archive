

n = int(input())

unsorted_nums = list(map(int, input().split()))

sorted_nums = sorted(unsorted_nums)


swaps = []
for i in range(n):

    if unsorted_nums[i] != sorted_nums[i]:
        j = i
        while j < n and unsorted_nums[j] != sorted_nums[i]:
            j += 1

        swaps.append(f'{i} {j}')

        unsorted_nums[i], unsorted_nums[j] = unsorted_nums[j], unsorted_nums[i]

print(len(swaps))
print(*swaps, sep='\n')
