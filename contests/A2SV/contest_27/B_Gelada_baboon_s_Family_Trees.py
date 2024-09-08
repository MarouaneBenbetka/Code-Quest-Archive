

n = int(input())

most_distant_relative = list(map(int, input().split()))


s = set()
cpt = 0

for i in range(n):
    if i+1 == most_distant_relative[i]:
        cpt += 1
    else:
        s.add(most_distant_relative[i])

print(cpt + len(s) // 2)
