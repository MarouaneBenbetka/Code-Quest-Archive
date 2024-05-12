n = input()
arr = map(int, input().split())
count = 0
log = False
for i in arr:
    if i == 1:
        log = False
    elif not log:
        count += 1
        log = True

print(count)
