

t = int(input())

for _ in range(t):
    n = int(input())
    s1 = input()

    s2 = ""

    i = 0
    while i < n:
        s2 += s1[i]
        for j in range(i+1, n):
            if s1[j] == s1[i]:
                i = j
                break
        i += 1

    print(s2)
