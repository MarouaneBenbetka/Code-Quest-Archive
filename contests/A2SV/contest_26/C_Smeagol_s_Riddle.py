
for _ in range(int(input())):
    s = input()

    if len(s) == 1:
        print(0)
    else:
        p1 = 0
        p2 = len(s) - 1

        cpt = 0
        while p1 < p2:
            if s[p1] != s[p2]:
                cpt += 1

            p1 += 1
            p2 -= 1

        print(cpt)
