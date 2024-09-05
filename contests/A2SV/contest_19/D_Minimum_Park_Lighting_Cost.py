from itertools import combinations

n, m = map(int, input().split())

parks = []
for _ in range(n):
    si, ti, ci = map(int, input().split())
    parks.append((si, ti, ci))

lights = []
for _ in range(m):
    ai, bi, pi, mi = map(int, input().split())
    lights.append((ai, bi, pi, mi))


def check(lights_on):
    light_coverage = [0] * 101
    for i in lights_on:
        ai, bi, pi, _ = lights[i]
        for j in range(ai, bi + 1):
            light_coverage[j] += pi

    for si, ti, ci in parks:
        for j in range(si, ti + 1):
            if light_coverage[j] < ci:
                return False
    return True


min_cost = float('inf')

for k in range(1, m + 1):
    for light_combination in combinations(range(m), k):
        if check(light_combination):
            cost = sum(lights[i][3] for i in light_combination)
            min_cost = min(min_cost, cost)

print(min_cost)
