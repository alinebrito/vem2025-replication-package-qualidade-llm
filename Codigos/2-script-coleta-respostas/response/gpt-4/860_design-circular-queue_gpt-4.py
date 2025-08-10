class Solution:
    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1 + self.size) % self.size]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size