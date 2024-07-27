s = input()
stk = []
res = 0
for i in s:
    if i == '(':
        stk.append(i)
    else:
        if stk:
            stk.pop()
            res += 2
        else:
            continue

print(res)
