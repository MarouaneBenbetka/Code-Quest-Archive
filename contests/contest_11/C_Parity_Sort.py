for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odd_items = set()
    even_items = set()

    for i in range(n):
        if a[i] % 2 == 0:
            even_items.add(i)
        else:
            odd_items.add(i)

    a.sort()

    for i in range(n):
        if a[i] % 2 == 0:
            if i not in even_items:
                print('NO')
                break
        else:
            if i not in odd_items:
                print('NO')
                break
    else:
        print('YES')
