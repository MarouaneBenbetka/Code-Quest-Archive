

for _ in range(int(input())):
    n = int(input())

    candies = list(map(int, input().split()))

    mihai = 0
    bianca = 0

    total = 0
    for candy in candies:
        if candy % 2 == 0:
            mihai += candy
        else:
            bianca += candy

    if bianca >= mihai:
        print("NO")
    else:
        print("YES")
