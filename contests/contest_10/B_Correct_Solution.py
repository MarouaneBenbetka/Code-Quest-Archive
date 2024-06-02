

a = sorted(input())
b = input()


if a[0] == '0':
    for i in range(1, len(a)):
        if a[i] != '0':
            a[0], a[i] = a[i], '0'
            break

print('OK' if "".join(a) == b else 'WRONG_ANSWER')
