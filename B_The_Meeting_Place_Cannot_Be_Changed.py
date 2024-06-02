n = int(input())

coordinates = list(map(int, input().split()))
speeds = list(map(int, input().split()))

left, right = 0, 10**9


def is_valid_time(t):
    min_location, max_location = 0, 10**9
    for i in range(n):
        min_location = max(min_location,    coordinates[i] - speeds[i]*t)
        max_location = min(max_location,  coordinates[i] + speeds[i]*t)
    return min_location <= max_location


while abs(right-left) > 1e-6:
    mid = (left+right)/2
    if is_valid_time(mid):
        right = mid
    else:
        left = mid

print(mid)
