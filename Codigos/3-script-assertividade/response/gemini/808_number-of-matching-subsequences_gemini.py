class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(s,t):
            i = 0
            j = 0
            while i<len(s) and j<len(t):
                if s[i]==t[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j==len(t):
                return True
            else:
                return False
        count = 0
        for i in words:
            if issubseq(s,i):
                count+=1
        return count