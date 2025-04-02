

for _ in range(int(input())):
    arr = sorted(map(int, input().split()))

    if arr[1] + arr[2] >= 10:
        print("YES")
    else:
        print("NO")
