class Solution:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x: int) -> None:
        self.in_stk.append(x)

    def pop(self) -> int:
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk.pop()

    def peek(self) -> int:
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    def empty(self) -> bool:
        return len(self.in_stk) == 0 and len(self.out_stk) == 0