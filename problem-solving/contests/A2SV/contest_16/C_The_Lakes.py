from collections import deque

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(row, col, grid, n, m):
    queue = deque([(row, col)])
    volume = 0

    while queue:
        r, c = queue.popleft()
        if grid[r][c] > 0:
            volume += grid[r][c]
            grid[r][c] = -1
            for xr, xc in moves:
                nr, nc = r + xr, c + xc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > 0:
                    queue.append((nr, nc))

    return volume


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        grid = []

        for _ in range(n):
            grid.append(list(map(int, input().split())))

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    ans = max(ans, bfs(i, j, grid, n, m))

        print(ans)


main()
