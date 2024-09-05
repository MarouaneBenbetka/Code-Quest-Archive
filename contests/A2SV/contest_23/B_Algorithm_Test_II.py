from collections import defaultdict, deque


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def insert_after(self, target_node, new_node):
        new_node.prev = target_node
        new_node.next = target_node.next
        if target_node.next:
            target_node.next.prev = new_node
        else:
            self.tail = new_node
        target_node.next = new_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def to_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next


q = int(input())

index = defaultdict(deque)
linked_list = LinkedList()

for _ in range(q):
    operation, *rest = input().split()

    if operation == "insert":
        x, y = map(int, rest)
        new_node = Node(x)

        if y not in index or not index[y]:
            linked_list.append(new_node)
            index[x].append(new_node)
        else:
            target_node = index[y][0]
            linked_list.insert_after(target_node, new_node)
            index[x].append(new_node)

    else:  # remove
        w = int(rest[0])

        if w in index and index[w]:
            node_to_remove = index[w].popleft()
            linked_list.remove(node_to_remove)

linked_list.to_list()
