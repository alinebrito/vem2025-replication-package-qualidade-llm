class Solution:
class MyStack:

    def __init__(self):
        self._queue1 = collections.deque()
        self._queue2 = collections.deque()

    def push(self, x: int) -> None:
        self._queue1.append(x)

    def pop(self) -> int:
        while len(self._queue1) > 1:
            self._queue2.append(self._queue1.popleft())
        top = self._queue1.popleft()
        self._queue1, self._queue2 = self._queue2, self._queue1
        return top

    def top(self) -> int:
        while len(self._queue1) > 1:
            self._queue2.append(self._queue1.popleft())
        top = self._queue1.popleft()
        self._queue2.append(top)
        self._queue1, self._queue2 = self._queue2, self._queue1
        return top

    def empty(self) -> bool:
        return len(self._queue1) == 0