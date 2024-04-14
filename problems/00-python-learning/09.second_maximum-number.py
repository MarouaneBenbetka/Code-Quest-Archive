# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    max1 = -200
    max2 = -200

    for score in arr:
        if score > max1:
            max2, max1 = max1, score
        elif score > max2 and score != max1:
            max2 = score

    print(max2)
