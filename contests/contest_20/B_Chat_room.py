
hello_mixed = input().lower()


word = 'hello'
curr = 0
for c in hello_mixed:
    if c == word[curr]:
        curr += 1

    if curr == len(word):
        print("YES")
        break
else:
    print("NO")
