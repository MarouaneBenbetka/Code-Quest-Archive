

for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1]:
        print(a[-1])
    else:
        print(a[0])
