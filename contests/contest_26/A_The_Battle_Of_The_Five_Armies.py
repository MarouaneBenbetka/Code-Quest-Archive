A, B, C, D, E = map(int, input().split())

M, N, O, P, Q = map(int, input().split())

group1 = A*M + B*N + C*O

group2 = D*P + E*Q

if group1 > group2:
    print("WIN")
elif group1 < group2:
    print("LOSE")
else:
    print("DRAW")
