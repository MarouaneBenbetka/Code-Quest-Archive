# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?isFullScreen=true


cpt_swaps = 0


def bubble_sort(a):
    global cpt_swaps
    n = len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                cpt_swaps += 1

    return a


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    a = bubble_sort(a)

    print(f"Array is sorted in {cpt_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
