
import math

for _ in range(int(input())):
    n = int(input())
    mat = []

    for _ in range(n):
        mat.append(list(map(int, input())))

    cpt = 0
    m = math.ceil(n/2)
    for i in range(m):
        for j in range(m):
            arr = [mat[i][j], mat[j][-i-1], mat[-i-1][-j-1], mat[-j-1][i]]
            # print(arr)
            # print((i, j), (j, -i-1), (-i-1, -j-1), (j, -i-1))
            if not len(set(arr)) == 1:
                ones = arr.count(1)
                zeros = arr.count(0)
                cpt += min(4-ones, 4-zeros)
                mat[i][j] = mat[j][-i-1] = mat[-i - 1][-j -
                                                       1] = mat[-j-1][i] = 1 if 4-ones < 4-zeros else 0

    print(cpt)
