import math
input()

colors = len(set(list(map(int, input().split()))))

print(math.factorial(colors))
