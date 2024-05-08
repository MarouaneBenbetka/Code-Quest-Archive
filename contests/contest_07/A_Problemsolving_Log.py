
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()

    cnt = Counter(s)

    cpt = 0

    for c in cnt:
        if cnt[c] >= ord(c) - ord('A') + 1:
            cpt += 1

    print(cpt)
