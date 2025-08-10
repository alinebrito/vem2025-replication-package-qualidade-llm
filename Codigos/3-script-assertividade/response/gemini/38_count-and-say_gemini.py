class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            count = 1
            temp = []
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    temp.append(str(count) + s[i - 1])
                    count = 1
            temp.append(str(count) + s[-1])
            s = ''.join(temp)
        return s