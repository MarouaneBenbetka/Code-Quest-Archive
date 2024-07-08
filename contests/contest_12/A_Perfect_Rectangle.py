
import math


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    x = sum(a)

    if math.ceil(math.sqrt(x)) == math.floor(math.sqrt(x)):
        print("YES")
    else:
        print("NO")
