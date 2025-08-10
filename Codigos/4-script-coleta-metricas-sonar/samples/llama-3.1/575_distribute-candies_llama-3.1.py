class Solution:
    def distributeCandies(self, candyType):
        return len(set(candyType)) if len(set(candyType)) <= len(candyType) // 2 else len(candyType) // 2