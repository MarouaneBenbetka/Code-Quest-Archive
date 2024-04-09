

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


# n, m = map(int, input().split())

# d = {}
# for _ in range(n):
#     name, ip = input().split()
#     d[ip] = name
# for _ in range(m):
#     command, ip = input().split()
#     print(command, ip, "#"+d[ip[:-1]])


# ================================================================================================================================================================


# for _ in range(int(input())):
#     n = int(input())
#     list = sorted(((int(x)-i, i)
#                    for i, x in enumerate(input().split())), reverse=True)

#     b_list = []
#     for i in range(0, n-3):
#         res = 0
#         l = 0
#         r = n
#         for b, i in list[i:i+3]:
#             res += b+i
#             r = min(r, i)
#             l = max(l, i)
#         b_list.append(res - l + r)

#     print(max(b_list))


# ================================================================================================================================================================


nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

p = 0
cpt = 0
res = []
for n in nums2:
    while p < len(nums1) and nums1[p] <= n:
        cpt += 1
        p += 1

    res.append(cpt)

print(*res)
