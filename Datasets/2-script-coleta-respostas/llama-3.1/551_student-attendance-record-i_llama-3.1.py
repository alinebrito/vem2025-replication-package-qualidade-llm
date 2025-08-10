class Solution:
    def checkRecord(self, s):
        return not ('LLL' in s or s.count('A') >= 2)