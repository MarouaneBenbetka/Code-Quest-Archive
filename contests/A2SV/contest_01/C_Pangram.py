

n = int(input())

s = input()

alphabet = set("abcdefghijklmnopqrstuvwxyz")
print("YES" if alphabet.issubset(set(s.lower())) else "NO")
