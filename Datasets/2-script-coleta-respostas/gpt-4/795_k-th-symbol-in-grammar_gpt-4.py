class Solution:
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        mid = 2 ** (n - 1) // 2
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 if self.kthGrammar(n - 1, k - mid) == 0 else 0