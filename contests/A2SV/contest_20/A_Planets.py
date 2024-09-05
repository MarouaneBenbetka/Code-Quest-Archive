from collections import Counter


for _ in range(int(input())):
    n, c = map(int, input().split())

    orbits = list(map(int, input().split()))

    planets_per_orbit = Counter(orbits).values()

    cost = 0
    for planets in planets_per_orbit:
        cost += min(planets, c)

    print(cost)
