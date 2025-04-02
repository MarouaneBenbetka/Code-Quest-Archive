n = int(input())

l = list(map(int, input().split()))

l.sort()


res = 0
cpt = 0
for i in range(n):
    if l[i] >= res:
        res += l[i]
        cpt += 1

print(cpt)
