from collections import deque

# Solution using a Queue as a "sliding window"
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.capacity = size
        self.Q = deque()

    def next(self, val: int) -> float:
        self.Q.append(val)
        if len(self.Q) > self.capacity:
            self.Q.popleft()
        return sum(self.Q) / len(self.Q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
