

n, t = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = 0

window = arr[0]
max_window = int(window <= t)

for right in range(1, n):
    window += arr[right]

    while window > t:
        window -= arr[left]
        left += 1
    # print(arr[left:right+1])
    max_window = max(max_window, right - left + 1)

print(max_window)
