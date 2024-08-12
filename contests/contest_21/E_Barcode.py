import sys
import threading


def main():

    n, m, x, y = map(int, input().split())

    bar_code = [input() for _ in range(n)]

    pfx_white = [0] * (m + 1)
    pfx_black = [0] * (m + 1)

    for j in range(m):
        white_px = sum(bar_code[i][j] == '.' for i in range(n))
        pfx_white[j+1] = pfx_white[j] + white_px
        pfx_black[j+1] = pfx_black[j] + n - white_px

    memo = {}

    def solve(curr_col, curr_color):
        if curr_col == m:
            return 0

        if (curr_col, curr_color) in memo:
            return memo[(curr_col, curr_color)]

        minn = float('inf')

        for end in range(curr_col + x, min(curr_col + y + 1, m + 1)):

            if curr_color == 'B':
                white_count = pfx_white[end] - pfx_white[curr_col]
                cost = white_count + solve(end, 'W')
            else:
                black_count = pfx_black[end] - pfx_black[curr_col]
                cost = black_count + solve(end, 'B')

            minn = min(minn, cost)

        memo[(curr_col, curr_color)] = minn
        return minn

    print(min(solve(0, 'B'), solve(0, 'W')))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
