def fill_matrix(n):
    mat = [[0] * n for _ in range(n)]

    s = 1
    e = n * n
    c = 1

    for i in range(1, n + 1):
        if i % 2 != 0:
            for j in range(1, n + 1):
                if c % 2 != 0:
                    mat[i-1][j-1] = s
                    s += 1
                else:
                    mat[i-1][j-1] = e
                    e -= 1
                c += 1
        else:
            for j in range(n, 0, -1):
                if c % 2 != 0:
                    mat[i-1][j-1] = s
                    s += 1
                else:
                    mat[i-1][j-1] = e
                    e -= 1
                c += 1

    for row in mat:
        print(*row)


for _ in range(int(input())):
    n = int(input())

    fill_matrix(n)
