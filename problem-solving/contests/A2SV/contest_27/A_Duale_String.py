

for _ in range(int(input())):
    s = input()

    if len(s) % 2:
        print("NO")
        continue

    is_duale = True

    mid = len(s)//2
    for i in range(mid):
        if s[i] != s[mid+i]:
            is_duale = False
            break

    print("YES" if is_duale else "NO")
