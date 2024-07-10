n, m = map(int, input().split())


flag = [input() for _ in range(n)]


check_horizontal = True

for i in range(n):
    if len(set(flag[i])) > 1:
        print("NO")
        exit()

for i in range(1, n):
    if flag[i] == flag[i-1]:
        print("NO")
        exit()

print("YES")
