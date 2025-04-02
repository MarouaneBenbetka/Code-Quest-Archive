from collections import deque


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(int(input())):
    n, m = map(int, input().split())

    grid = []
    for i in range(n):
        grid.append(list(input()))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == '.':
                            grid[ni][nj] = '#'

    queue = deque()
    if grid[n-1][m-1] == '.':
        queue.append((n-1, m-1))
        grid[n-1][m-1] = '+'

    reached_g = 0
    found_b = False
    total_g = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G':
                total_g += 1

    while queue:
        x, y = queue.popleft()
        for di, dj in directions:
            nx, ny = x + di, y + dj
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 'G':
                    reached_g += 1
                    grid[nx][ny] = '+'
                    queue.append((nx, ny))
                elif grid[nx][ny] == '.':
                    grid[nx][ny] = '+'
                    queue.append((nx, ny))
                elif grid[nx][ny] == 'B':
                    found_b = True

    if reached_g == total_g and not found_b:
        print("Yes")
    else:
        print("No")
