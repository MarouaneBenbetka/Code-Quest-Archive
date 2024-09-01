

seq = input()


maxx = 0
count = 0


for c in seq:
    if c != 'O':
        count = 0
    else:
        count += 1
        maxx = max(maxx, count)

print(maxx)
