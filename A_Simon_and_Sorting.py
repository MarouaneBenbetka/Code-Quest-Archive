

for _ in range(int(input())):
    abc = input()

    abc_s = ''.join(sorted(abc))
    cpt = 0
    for i in range(len(abc)):
        if abc_s[i] != abc[i]:
            cpt += 1

        if cpt > 2:
            break

    if cpt <= 2:
        print("YES")
    else:
        print("NO")
