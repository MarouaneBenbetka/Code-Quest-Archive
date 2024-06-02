
for _ in range(int(input())):
    s = list(input())

    if not s:
        print('NO')
        continue

    prev = s[0]
    for i in range(1, len(s)):
        if s[i] != prev:
            s[0], s[i] = s[i], s[0]
            print('YES')
            print(''.join(s))
            break
    else:
        print('NO')
