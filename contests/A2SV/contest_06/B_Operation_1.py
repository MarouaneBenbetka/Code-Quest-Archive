n, m = map(int, input().split())


res = n//2 + n % 2
cpt = 0
max_cpt = res - n % 2
while res % m != 0 and cpt < max_cpt:
    res += 1
    cpt += 1

if res % m == 0:
    print(res)
else:
    print(-1)
