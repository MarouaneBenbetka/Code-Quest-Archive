

# monotonic_stack = []

# nb_rearagement = 0
# for _ in range(2*int(input())):
#     s = input().split()
#     if len(s) > 1:
#         command = "add"
#         value = int(s[1])
#     else:
#         command = "remove"

#     if command == "remove":
#         if monotonic_stack:
#             monotonic_stack.pop()
#     else:

#         if monotonic_stack and value > monotonic_stack[-1]:
#             monotonic_stack.append(value)
#             monotonic_stack.sort(reverse=True)
#             nb_rearagement += 1
#         else:
#             monotonic_stack.append(value)


# print(nb_rearagement)


x = int(input())
s = []
p = 1
count = 0

for i in range(2 * x):
    a = input().split()
    if "add" == a[0]:
        v = int(a[1])
        s.append(v)
    else:
        if s:
            x = s.pop()
            if x != p:
                count += 1
                s = []
        p += 1

print(count)
