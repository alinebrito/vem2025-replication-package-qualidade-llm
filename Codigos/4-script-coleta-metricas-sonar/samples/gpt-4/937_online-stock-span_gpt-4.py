class Solution:
    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price):
        span = 1  
        while self.prices and self.prices[-1] <= price:
            span += self.spans.pop()
            self.prices.pop()
        self.prices.append(price)
        self.spans.append(span)
        return span  