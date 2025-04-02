

# https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

item = arr.pop()


for i in range(n-2, -1, -1):
    if arr[i] > item:
        print(*arr[:i+1], arr[i], *arr[i+1:])
    else:
        print(*arr[:i+1], item, *arr[i+1:])
        break
else:
    print(item, *arr[i:])
