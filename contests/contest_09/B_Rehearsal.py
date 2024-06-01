n = int(input())

arr = []

for x in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])


arr.sort()
l, r = 0, len(arr)-1
ans = 0

while l <= r:
    ans = max(ans, arr[l][0] + arr[r][0])

    if arr[l][1] == arr[r][1]:
        r -= 1
        l += 1
    elif arr[l][1] < arr[r][1]:
        arr[r][1] -= arr[l][1]
        l += 1
    else:
        arr[l][1] -= arr[r][1]
        r -= 1


print(ans)
