
for _ in range(int(input())):
    n, a, b = map(int, input().split())

    n_b, n_a = divmod(n, 2)
    if b <= 2*a:
        print(a*n_a+b*n_b)
    else:
        print(a*n)
