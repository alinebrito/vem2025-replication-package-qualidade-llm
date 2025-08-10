class Solution:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)