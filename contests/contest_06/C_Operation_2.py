from collections import deque


def count_min_op(a, b):
    seen = set()
    BFS_queue = deque([(a, 0)])
    while BFS_queue:
        current, ops = BFS_queue.popleft()

        if current == b:
            return ops

        if current < b and current * 2 not in seen:
            BFS_queue.append((current * 2, ops + 1))
            seen.add(current * 2)

        if current - 1 > 0 and current - 1 not in seen:
            BFS_queue.append((current - 1, ops + 1))
            seen.add(current - 1)

    return -1


# Example usage:
a, b = map(int, input().split())
print(count_min_op(a, b))
