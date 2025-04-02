n = int(input())

arr = list(map(int, input().split()))

s_arr = sorted(arr)

res = 0

for i in range(n):
    if arr[i] != s_arr[i]:
        res += 1

print(res - 1)
