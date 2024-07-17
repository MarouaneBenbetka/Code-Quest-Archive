from collections import Counter
n = int(input())

boxes = list(map(int, input().split()))


cnt = Counter(boxes)

print(max(cnt.values()))
