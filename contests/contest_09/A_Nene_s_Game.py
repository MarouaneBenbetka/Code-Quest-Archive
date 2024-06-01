

for _ in range(int(input())):
    k, q = map(int, input().split())
    a = int(input().split()[0])
    print(*[query if query < a else a -
          1 for query in map(int, input().split())])
