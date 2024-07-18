n = int(input())


nums = list(map(int, input().split()))


p1 = []
p2 = []
p3 = []

for num in nums:
    if num > 0:
        p1.append(num)
    elif num < 0:
        p2.append(num)
    else:
        p3.append(num)


if len(p2) > 1:
    if len(p1) == 0:
        p1.extend(p2[1:3])
        p3.extend(p2[3:])
    else:
        p3.extend(p2[1:])

    p2 = p2[:1]
print(len(p2), *p2)
print(len(p1), *p1)
print(len(p3), *p3)
