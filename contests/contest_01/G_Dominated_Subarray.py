T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    last_occurrence = {}
    min_length = float('inf')
    for i, num in enumerate(a):
        if num in last_occurrence:
            min_length = min(min_length, i - last_occurrence[num] + 1)
        last_occurrence[num] = i
    print(min_length if min_length != float('inf') else -1)
