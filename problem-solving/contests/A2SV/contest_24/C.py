import sys
import threading


def rec(array, possible):

    ssum = 0
    mmin = float('inf')
    mmax = float('-inf')

    for num in array:
        ssum += num
        if num < mmin:
            mmin = num
        if num > mmax:
            mmax = num

    possible.add(ssum)
    if mmin == mmax:
        return

    avg = (mmin+mmax)//2

    left = []
    right = []

    for num in array:
        if num <= avg:
            left.append(num)
        else:
            right.append(num)

    rec(left, possible)
    rec(right, possible)


def main():

    for _ in range(int(input())):

        n, q = map(int, input().split())

        nums = list(map(int, input().split()))

        possible = set()

        rec(nums, possible)
        for _ in range(q):
            if int(input()) in possible:
                print('Yes')
            else:
                print('No')


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
