from collections import Counter

n, k = map(int, input().split())
numbers = sorted(map(int, input().split()))

prefix_sum = [0]

for i in range(n):
    prefix_sum.append(prefix_sum[-1] + numbers[i])


def cost(left, curr):
    return (curr-left)*numbers[curr] - (prefix_sum[curr]-prefix_sum[left])


ans = numbers[0]
max_cpt = 1


for i in range(1, n):
    low = 0
    high = i

    while low < high - 1:
        mid = (low+high)//2
        if cost(mid, i) <= k:
            high = mid
        else:
            low = mid+1

    if cost(low, i) <= k:
        if i-low+1 > max_cpt:
            max_cpt = i-low+1
            ans = numbers[i]
    elif cost(high, i) <= k:
        if i-high+1 > max_cpt:
            max_cpt = i-high+1
            ans = numbers[i]

print(max_cpt, ans)
