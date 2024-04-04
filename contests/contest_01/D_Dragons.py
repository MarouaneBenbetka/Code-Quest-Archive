s, n = map(int, input().split())
dragons = [list(map(int, input().split())) for _ in range(n)]
dragons.sort()

for dragon in dragons:
    if s > dragon[0]:
        s += dragon[1]
    else:
        print("NO")
        break
else:
    print("YES")
