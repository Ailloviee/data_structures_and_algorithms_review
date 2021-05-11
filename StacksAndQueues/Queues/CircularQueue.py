class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.head = self.tail = 0
        self.capacity = k
        self.Q = [-1 for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        else:
            self.size += 1
            if self.tail == self.capacity - 1:
                self.tail = 0
            else:
                self.tail += 1
            if self.size == 1:
                self.head = self.tail
            self.Q[self.tail] = value
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            self.size -= 1
            if self.head == self.capacity - 1:
                self.head = 0
            else:
                self.head += 1
            return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.Q[self.head]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.Q[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
