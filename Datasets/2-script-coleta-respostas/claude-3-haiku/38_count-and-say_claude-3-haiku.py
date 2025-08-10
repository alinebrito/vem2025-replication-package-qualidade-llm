class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            say = ''
            count = 1
            for i in range(len(s)):
                if i == len(s)-1 or s[i] != s[i+1]:
                    say += str(count) + s[i]
                    count = 1
                else:
                    count += 1
            s = say
        return s