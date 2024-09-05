
l, r = map(int, input().split())

diff = l ^ r

highest = 1

while diff > 0:
    highest <<= 1
    highest |= 1

    diff >>= 1

print(highest >> 1)
