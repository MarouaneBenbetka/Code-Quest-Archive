m = []
for _ in range(5):
    m.append(list(map(int, input().split())))

one_pos = [(row_idx, col_idx) for row_idx, row in enumerate(m)
           for col_idx, val in enumerate(row) if val == 1][0]

moves = abs(2 - one_pos[0]) + abs(2 - one_pos[1])

print(moves)
