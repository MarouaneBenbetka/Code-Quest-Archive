n, d = map(int, input().split())

track = list(map(int, input()))


curr = 0
next = 0

i = 0
cpt = 0

while i < len(track):

    i = curr
    while i < len(track)-1 and i < curr + d:
        i += 1
        if track[i] == 1:
            next = i
    if next == curr:
        print(-1)
        exit()

    curr = next
    cpt += 1

    if curr == len(track)-1:
        break

print(cpt)
