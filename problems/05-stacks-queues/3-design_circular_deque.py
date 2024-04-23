# https://leetcode.com/problems/design-circular-deque/


class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None]*k
        self.head = None
        self.tail = None
        self.k = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.head is None:
            self.head = 0
            self.tail = 0
        else:
            new_head = (self.head - 1) % self.k
            if new_head == self.tail:
                return False
            else:
                self.head = new_head

        self.deque[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.head is None:
            self.head = 0
            self.tail = 0
        else:
            new_tail = (self.tail+1) % self.k
            if new_tail == self.head:
                return False
            else:
                self.tail = new_tail

        self.deque[self.tail] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = (self.head+1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = (self.tail-1) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.head is None:
            return -1

        return self.deque[self.head]

    def getRear(self) -> int:
        if self.tail is None:
            return -1

        return self.deque[self.tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
