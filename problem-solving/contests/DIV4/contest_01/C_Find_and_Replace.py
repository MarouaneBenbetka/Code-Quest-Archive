

for _ in range(int(input())):

    n = int(input())
    s = input()

    mapping = {s[0]: 1}

    for i in range(1, n):
        if s[i] not in mapping:
            mapping[s[i]] = ~mapping[s[i-1]]
        else:
            if mapping[s[i]] == mapping[s[i-1]]:
                print("NO")
                break
    else:
        print("YES")
