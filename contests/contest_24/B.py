

n = int(input())

angles = [int(input()) for _ in range(n)]

if n == 1 and angles[0] != 0:
    print('NO')
    exit()


def rec(index, ssum):
    if index == n:
        return ssum % 360 == 0

    return rec(index+1, (ssum+angles[index]) % 360) or rec(index+1, (ssum-angles[index]) % 360)


print("YES" if rec(0, 0) else "NO")
