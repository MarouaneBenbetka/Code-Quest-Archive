s = input()


stk = []
i = 0
while i < len(s):
    if s[i] == "<":
        i += 2
        if stk:
            stk.pop()
    else:
        stk.append(s[i])
        i += 1

print("".join(stk))
