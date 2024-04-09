# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[x_i, x_y,x_z] for x_i in range(x+1) for x_y in range(y+1) for x_z in range(z+1) if x_i + x_y + x_z != n])