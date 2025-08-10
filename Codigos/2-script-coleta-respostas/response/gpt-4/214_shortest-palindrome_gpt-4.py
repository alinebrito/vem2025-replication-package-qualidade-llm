class Solution:
    def shortestPalindrome(self, s):
        r = s[::-1]
        l = s + "#" + r
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            if l[i] == l[j]:
                j += 1
            p[i] = j
        return r[:len(s) - p[-1]] + s