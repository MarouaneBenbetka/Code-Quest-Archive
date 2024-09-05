n = int(input())
hist = list(map(int, input().split()))

stack = []
maxi = 0

for i in range(n):
    while stack and hist[i] < hist[stack[-1]]:
        height = hist[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        maxi = max(maxi, min(height, width))

    stack.append(i)

while stack:
    height = hist[stack.pop()]
    width = n if not stack else n - stack[-1] - 1
    maxi = max(maxi, min(height, width))

print(maxi)
