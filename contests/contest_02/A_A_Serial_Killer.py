# Bismillahir Rahmanir Rahim

def main():
    f, l = input().split()
    n = int(input())
    print(f, l)

    for _ in range(n):
        next_name, later_name = input().split()
        if f == next_name:
            f = later_name
            print(f, l)
        elif f == later_name:
            f = next_name
            print(f, l)
        elif l == next_name:
            l = later_name
            print(f, l)
        else:
            l = next_name
            print(f, l)


if __name__ == "__main__":
    main()
