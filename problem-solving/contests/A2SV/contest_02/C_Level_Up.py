

def can_betty_progress(s, challenges):
    challenges.sort()

    # Traverse sorted challenges
    for difficulty, bonus in challenges:
        if s > difficulty:
            s += bonus
        else:
            return "NO"
    return "YES"


s, n = map(int, input().split())


challenges = []


for _ in range(n):
    x, y = map(int, input().split())

    challenges.append((x, y))


print(can_betty_progress(s, challenges))
