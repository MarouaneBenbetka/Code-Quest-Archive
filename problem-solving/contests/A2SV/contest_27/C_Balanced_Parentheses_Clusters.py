

for _ in range(int(input())):

    n = int(input())
    paranthesis = input()

    print(n - paranthesis.count(")("))
