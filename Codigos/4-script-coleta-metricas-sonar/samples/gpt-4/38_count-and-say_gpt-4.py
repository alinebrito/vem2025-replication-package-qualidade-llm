class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(1, n):
            next_s = ''
            count = 1
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    next_s += str(count) + s[j - 1]
                    count = 1
            next_s += str(count) + s[-1]
            s = next_s
        return s