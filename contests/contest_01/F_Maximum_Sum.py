t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()  # Sort to easily pick minimum and maximum values
    # Initial sum of the array
    total_sum = sum(a)
    # Remove two minimum values k times
    i = 0
    while k > 0 and i < n - 1:  # Ensure there are elements to operate on
        # Deduct the two smallest elements at each step
        total_sum -= a[i] + a[i + 1]
        i += 2
        k -= 1
    # If there's an odd operation left, remove the current minimum (next in line)
    if k > 0:
        total_sum -= a[i]
    print(total_sum)
