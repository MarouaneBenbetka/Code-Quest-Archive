import sys
import threading


def solve(curr_col, prev_color, x, y, dp, pfx_white, pfx_black, m):
    if curr_col == m:
        return 0

    if (curr_col, prev_color) in dp:
        return dp[(curr_col, prev_color)]

    minn = float('inf')

    for end in range(curr_col + x, min(curr_col + y + 1, m + 1)):
        white_count, black_count = pfx_white[end] - \
            pfx_white[curr_col], pfx_black[end] - pfx_black[curr_col]

        if prev_color == 'B':
            cost = white_count + \
                solve(end, 'W', x, y, dp, pfx_white, pfx_black, m)
        else:
            cost = black_count + \
                solve(end, 'B', x, y, dp, pfx_white, pfx_black, m)

        minn = min(minn, cost)

    dp[(curr_col, prev_color)] = minn
    return minn


def main():

    n, m, x, y = map(int, input().split())

    bar_code = [input() for _ in range(n)]

    pfx_white = [0] * (m + 1)
    pfx_black = [0] * (m + 1)

    for j in range(1, m + 1):
        white_px = sum(bar_code[i][j-1] == '.' for i in range(n))
        pfx_white[j] = pfx_white[j - 1] + white_px
        pfx_black[j] = pfx_black[j - 1] + n - white_px

    dp = {}

    print(min(solve(0, 'B', x, y, dp,  pfx_white, pfx_black, m),
          solve(0, 'W',  x, y, dp, pfx_white, pfx_black, m)))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
