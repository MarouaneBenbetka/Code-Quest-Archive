from heapq import heappush, heappop, heapify

n = int(input())


logs = []
for _ in range(n):
    seq = input().split()
    operation = seq[0]
    result = None
    if len(seq) > 1:
        result = int(seq[1])

    logs.append((operation, result))

heap = []


new_log = []
for operation, val in logs:
    if operation == 'insert':
        heappush(heap, val)
        new_log.append(('insert', val))
    elif operation == 'getMin':
        # remove all the elments that are less than X
        while heap and heap[0] < val:
            heappop(heap)
            new_log.append(('removeMin', None))

        # X is in the heap
        if not heap or heap[0] > val:
            heappush(heap, val)
            new_log.append(('insert', val))

        new_log.append(('getMin', val))

    elif operation == 'removeMin':
        if not heap:
            heappush(heap, 1)
            new_log.append(('insert', 1))
        heappop(heap)
        new_log.append(('removeMin', None))

print(len(new_log))

for operation, val in new_log:
    if operation == 'removeMin':
        print(operation)
    else:
        print(operation, val)
