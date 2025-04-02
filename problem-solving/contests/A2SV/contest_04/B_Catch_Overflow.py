lines = int(input())
stack = [1]
x = 0
limit = pow(2, 32)

for _ in range(lines):
    command = input().split()

    if command[0] == "for":
        num = min(stack[-1] * int(command[1]), limit)
        stack.append(num)

    elif command[0] == "add":
        x += stack[-1]

    else:
        stack.pop()

    if x >= limit:
        x = "OVERFLOW!!!"
        break

print(x)
