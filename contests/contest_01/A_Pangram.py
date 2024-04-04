def is_pangram(n, string):
    string = string.lower()

    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    unique_letters = set(string)

    if alphabet.issubset(unique_letters):
        print("YES")
    else:
        return print("NO")


n = int(input())
string = input()
is_pangram(n, string)
