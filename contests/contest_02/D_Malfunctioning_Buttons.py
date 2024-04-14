t = int(input())
for _ in range(t):
    s = input().strip() + "#"
    v = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            i += 2
        else:
            v.append(s[i])
            i += 1

    v.sort()
    st = set(v[1:])
    for char in sorted(st):
        print(char, end="")
    print()
