

for _ in range(int(input())):
    n = int(input())
    candies = list(map(int, input().split()))

    left, right = 0, n-1
    alice = 0
    bob = 0

    alice_cpt = 0
    bob_cpt = 0

    res = 0

    while left <= right:
        if alice <= bob:
            alice += candies[left]
            alice_cpt += 1
            left += 1
        else:
            bob += candies[right]
            bob_cpt += 1
            right -= 1
        if alice == bob:
            res = alice_cpt+bob_cpt

    print(res)
