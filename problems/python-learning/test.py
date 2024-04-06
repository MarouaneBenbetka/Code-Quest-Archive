

# n = int(input())

# l = map(int, input().split())


# print(sum(l) / n)

# ================================================================================================================================================================

# n = int(input())

# l = map(int, input().split())

# if any(answer == 1 for answer in l):
#     print("HARD")
# else:
#     print("EASY")


# ================================================================================================================================================================


n, m = map(int, input().split())

d = {}
for _ in range(n):
    name, ip = input().split()
    d[ip] = name
for _ in range(m):
    command, ip = input().split()
    print(command, ip, "#"+d[ip[:-1]])
