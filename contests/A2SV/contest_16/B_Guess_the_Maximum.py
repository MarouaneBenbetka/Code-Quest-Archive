

for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))

    k = min(max(arr[i], arr[i+1]) for i in range(n-1)) - 1
    print(k)
