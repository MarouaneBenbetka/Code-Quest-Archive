from collections import deque


class UnionFind:

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

        # linked list maybe : (
        self.head = list(range(size))
        self.tail = list(range(size))
        self.next = [-1] * size

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 != parent2:
            if self.rank[parent1] > self.rank[parent2]:
                self.parent[parent2] = parent1
                self.rank[parent1] += self.rank[parent2]

                self.next[self.tail[parent1]] = self.head[parent2]
                self.tail[parent1] = self.tail[parent2]

            else:
                self.parent[parent1] = parent2

                if self.rank[parent1] == self.rank[parent2]:
                    self.rank[parent2] += 1

                self.next[self.tail[parent2]] = self.head[parent1]
                self.tail[parent2] = self.tail[parent1]
            return True
        return False


n = int(input())
uf = UnionFind(n)
for _ in range(n - 1):
    x, y = map(int, input().split())
    uf.union(x - 1, y - 1)

root = uf.find(0)
current = uf.head[root]
result = deque()

while current != -1:
    result.appendleft(current + 1)
    current = uf.next[current]

print(*result)
