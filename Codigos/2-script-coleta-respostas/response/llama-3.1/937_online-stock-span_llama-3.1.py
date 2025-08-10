class Solution:
 def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            span +=1
            self.stack.pop()
        self.stack.append(len(self.prices) - 1)
        return span