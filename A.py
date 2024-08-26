

num = input()

if any(digit in '02356789' for digit in num):
    print('NO')
    exit()


arr = num.split('1')

if num[0] != '1':
    print('NO')
    exit()

if any(len(group) >= 3 for group in arr):
    print('NO')
    exit()

print('YES')
