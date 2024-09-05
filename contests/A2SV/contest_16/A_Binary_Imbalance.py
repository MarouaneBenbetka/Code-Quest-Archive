
for _ in range(int(input())):
    n = int(input())
    s = input()

    if s.count('0') > s.count('1'):
        print('YES')
    elif '01' in s or '10' in s:
        print('YES')
    else:
        print('NO')
