n, m = map(int, input().split())


A = []

for i in range(n):
    A.append(list(map(int, input().split())))

visited = set()
operation = []
for i in range(n):
    for j in range(m):
        if A[i][j] == 1:
            if j+1 < m and i+1 < n and A[i][j+1] == 1 and A[i+1][j] == 1 and A[i+1][j+1] == 1:
                visited.add((i, j))
                visited.add((i, j+1))
                visited.add((i+1, j))
                visited.add((i+1, j+1))
                operation.append((i, j))
            else:
                if (i, j) not in visited:
                    print(-1)
                    exit()


print(len(operation))
for i, j in operation:
    print(i+1, j+1)
