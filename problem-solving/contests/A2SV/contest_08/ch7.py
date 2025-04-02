

n, m, k = map(int, input().split())

a = sorted(set(map(int, input())))
b = sorted(set(map(int, input())))


arr_a = list(range(1, k+1))
arr_b = list(range(1, k+1))


for item in a:
    if 0 < item and item <= k:
        arr_a[item-1] = 1


for item in b:
    if 0 < item and item <= k:
        arr_b[item-1] = 1


def sum_arr(arr1, arr2):
    return [a | b for a, b in zip(arr1, arr2)]


def xor(arr1, arr2):
    return [a ^ b for a, b in zip(arr1, arr2)]


if sum_arr(arr_a, arr_b).count(1) == k and arr_a.count(1) > k//2 and arr_b.count(1) > k//2 and xor(arr_a, arr_b).count(1) > k // 2:
    print(1)
else:
    print(0)
