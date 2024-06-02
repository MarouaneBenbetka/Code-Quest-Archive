from collections import deque

n, q = map(int, input().split())

a = deque(map(int, input().split()))

if q == 0:
    exit()

iterations = [int(input())-1 for _ in range(q)]

save = []


max_el = max(a)
max_index = -1


for i in range(n):
    A, B = a.popleft(), a.popleft()
    save.append((A, B))

    if A > B:
        a.appendleft(A)
        a.append(B)

        if A == max_el:
            max_index = i
            break

    else:
        a.appendleft(B)
        a.append(A)

        if B > max_el:
            max_index = i
            break


for it in iterations:
    if it < max_index:
        print(*save[it])
    else:
        relative_index = (it - max_index - 1) % (n - 1) + 1

        print(max_el, a[relative_index])
